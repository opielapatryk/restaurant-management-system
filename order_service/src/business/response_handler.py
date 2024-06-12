# BUILTIN modules
from uuid import UUID
from typing import Optional

# Third party modules
from loguru import logger
from httpx import AsyncClient, ConnectTimeout

# Local modules
from ..core.setup import config
from ..repository.interface import IRepository
from ..tools.url_cache import UrlServiceCache
from .models import KitchenPayload, DeliveryPayload
from ..repository.models import Status, OrderModel, StateUpdateSchema


# ------------------------------------------------------------------------
#
class OrderPaymentResponseLogic:
    """
    This class implements the OrderService business logic layer
    for RabbitMQ response messages.

    :ivar repo: DB repository.
    :type repo: `IRepository`
    """

    # ---------------------------------------------------------
    #
    def __init__(self, repository: IRepository):
        """ The class initializer.

        :param repository: Data layer handler object.
        """
        self.repo = repository

    # ---------------------------------------------------------
    #
    async def _update_order_in_db(self, order: OrderModel,
                                  service: Optional[str] = None):
        """ Update Order in DB.

        :param order: Current Order.
        :param service: Updated service.
        """
        successful = await self.repo.update(order)

        if not successful:
            errmsg = f"Failed updating order '{order.id}' in api_db.orders"
            raise RuntimeError(errmsg)

        log = getattr(logger, (
            'error' if order.status == 'paymentFailed' else 'info'
        ))

        match service:
            case 'KitchenService':
                txt = (f"Stored kitchen_id '{order.kitchen_id}' "
                       f"in DB for order '{order.id}'.")
            case 'DeliveryService':
                txt = (f"Stored delivery_id '{order.delivery_id}' "
                       f"in DB for order '{order.id}'.")
            case _:
                txt = (f"Stored status '{order.status.value}' "
                       f"in DB for order '{order.id}'.")

        log(txt)

    # ---------------------------------------------------------
    #
    async def _handle_successful_payment(self, message: dict, order: OrderModel):
        """ Payment was successful, so get Customer Address and request DeliveryService work.

        :param message: PaymentService response message.
        :param order: Current Order.
        """
        service = 'CustomerService'
        cache = UrlServiceCache(config.redis_url)

        try:
            root = await cache.get(service)

            # Get Customer Address information.
            async with AsyncClient() as client:
                url = f"{root}/api/v1/customers/{order.customer_id}/address"
                resp = await client.get(url=url, timeout=config.url_timeout)

            if resp.status_code != 200:
                errmsg = (f"Failed {service} POST request for URL {url} - "
                          f"[{resp.status_code}: {resp.json()['detail']}].")
                raise RuntimeError(errmsg)

            payload = DeliveryPayload(metadata=message['metadata'],
                                      address=resp.json(), items=order.items)

            service = 'DeliveryService'
            root = await cache.get(service)

            # Request DeliveryService work.
            async with AsyncClient() as client:
                url = f"{root}/api/v1/deliveries"
                resp = await client.post(timeout=config.url_timeout,
                                         data=payload.model_dump_json(),
                                         url=url, headers=config.hdr_data)

            if resp.status_code != 202:
                errmsg = (f"Failed {service} POST request for URL {url} - "
                          f"[{resp.status_code}: {resp.json()['detail']}].")
                raise RuntimeError(errmsg)

            data = resp.json()
            order.delivery_id = UUID(data['delivery_id'])
            order.updated.append(StateUpdateSchema(status=order.status))
            await self._update_order_in_db(order, service)

        except ConnectTimeout:
            errmsg = f'No connection with {service} on URL {url}'
            raise ConnectionError(errmsg)

        finally:
            await cache.close()

    # ---------------------------------------------------------
    #
    async def _handle_delivery_ready(self, message: dict, order: OrderModel):
        """ Delivery is ready for pickup so request KitchenService work.

        :param message: DeliveryService metadata response message.
        :param order: Current Order.
        """
        cache = UrlServiceCache(config.redis_url)
        payload = KitchenPayload(metadata=message['metadata'], **order.model_dump())

        try:
            service = 'KitchenService'
            root = await cache.get(service)

            # Request KitchenService work.
            async with AsyncClient() as client:
                url = f"{root}/api/v1/kitchen"
                resp = await client.post(timeout=config.url_timeout,
                                         data=payload.model_dump_json(),
                                         url=url, headers=config.hdr_data)

            if resp.status_code != 202:
                errmsg = (f"Failed KitchenService POST request for URL {url} "
                          f"- [{resp.status_code}: {resp.json()['detail']}].")
                raise RuntimeError(errmsg)

            data = resp.json()
            order.kitchen_id = UUID(data['kitchen_id'])
            order.updated.append(StateUpdateSchema(status=order.status))
            await self._update_order_in_db(order, service)

        except ConnectTimeout:
            errmsg = f'No connection with KitchenService on URL {url}'
            raise ConnectionError(errmsg)

        finally:
            await cache.close()

    # ---------------------------------------------------------
    #
    async def process_response(self, message: dict):
        """ Process response message data.

        Implemented business logic:
          - Every received message state is updated in DB.
          - When status is 'paymentPaid':
              - Trigger DeliveryService work.
          - When status is 'driverAvailable':
              - Trigger KitchenService work.

        :param message: Response message data.
        """
        status = Status(message['status'])
        order_id = UUID(message['metadata']['order_id'])

        try:
            # Read specified Order from DB.
            order = await self.repo.read(order_id)

            if not order:
                raise RuntimeError(f"Order '{order_id}' not found in api_db.orders.")

            order.status = status
            order.updated.append(StateUpdateSchema(status=order.status))
            await self._update_order_in_db(order)

            if status == Status.PAID:
                await self._handle_successful_payment(message, order)

            elif status == Status.DRAV:
                await self._handle_delivery_ready(message, order)

        except RuntimeError as why:
            logger.error(f'{why}')

        except ConnectionError as why:
            logger.critical(f'{why}')

        except BaseException as why:
            logger.critical(f'Failed processing response {status=} => {why}')