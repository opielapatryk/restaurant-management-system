# BUILTIN modules
from uuid import UUID
from datetime import datetime
from typing import Optional, List

# Third party modules
from pydantic import BaseModel, ConfigDict, Field

# Local modules
from ...repository.models import Status, OrderItems
from ...repository.documentation import order_documentation as order_doc


# -----------------------------------------------------------------------------
#
class NotFoundError(BaseModel):
    """ Define model for the http 404 exception (Not Found).

    :ivar detail: The detailed exception reason.
    """
    detail: str = "Order not found in DB"


class FailedUpdateError(BaseModel):
    """ Define model for the http 400 exception (Unprocessable Entity).

    :ivar detail: The detailed exception reason.
    """
    detail: str = "Failed updating Order in DB"


class ConnectError(BaseModel):
    """ Define model for the http 500 exception (INTERNAL_SERVER_ERROR).

    :ivar detail: The detailed exception reason.
    """
    detail: str = "Failed to connect to internal MicroService"


class HealthStatusError(BaseModel):
    """ Define model for the http 500 exception (INTERNAL_SERVER_ERROR).

    :ivar detail: The detailed exception reason.
    """
    detail: str = "HEALTH: resource connection(s) are down"


# ---------------------------------------------------------
#
class OrderPayload(OrderItems):
    """ Payload parameters required when creating an order.

    :ivar customer_id: Customer identity.
    """
    customer_id: UUID = Field(**order_doc['customer_id'])


# ---------------------------------------------------------
#
class OrderResponse(OrderItems):
    """ Expected default order response parameters.

    :ivar id: Order identity.
    :ivar status: Current order status.
    :ivar created: Datetime for created order.
    :ivar customer_id: Customer identity.
    :ivar kitchen_id: Kitchen identity.
    :ivar delivery_id: Delivery identity.
    """
    id: UUID = Field(**order_doc['id'])
    status: Status = Field(**order_doc['status'])
    created: datetime = Field(**order_doc['created'])
    customer_id: UUID = Field(**order_doc['customer_id'])
    kitchen_id: Optional[UUID] = Field(**order_doc['kitchen_id'])
    delivery_id: Optional[UUID] = Field(**order_doc['delivery_id'])


# ------------------------------------------------------------------------
#
class ValidStatus(BaseModel):
    """ Used for validation of received status responses.

    :ivar status: Current order status.
    """
    status: Status