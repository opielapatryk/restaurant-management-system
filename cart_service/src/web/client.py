import grpc
import logging
import os
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
from . import order_pb2
from . import order_pb2_grpc
import uuid


class OrderClient:
    def __init__(self, host=os.getenv('ORDER_GRPC', 'localhost'), port=50051):
        self.channel = grpc.insecure_channel(f'{host}:{port}')
        self.stub = order_pb2_grpc.OrderServiceStub(self.channel)

    def create_order(self, order):
        try:
            # Parse the created string into a datetime object
            created_datetime = datetime.fromisoformat(order['created'])

            request = order_pb2.Order(
                id=order['_id'],
                items=[order_pb2.Item(product=item['product'], quantity=item['quantity']) for item in order['items']],
                status=order['status'],
                created=Timestamp(seconds=int(created_datetime.timestamp())),
                customer_id=order['customer_id'],
                kitchen_id=order['kitchen_id'],
                delivery_id=order['delivery_id']
            )

            response = self.stub.CreateOrder(request)
            return response
        except grpc.RpcError as e:
            logging.error(f"Error occurred: {e}")
            return None
def create_order():
    client = OrderClient()
    generated_uuid = str(uuid.uuid4())

    response = client.create_order({
        "items": [
            {
                "product": "pizza",
                "quantity": 1
            }
        ],
        "_id": generated_uuid,
        "status": "created",
        "created": "2023-03-10T12:15:23.123234",  # Corrected the format
        "customer_id": "f2861560-e9ed-4463-955f-0c55c3b416fb",
        "kitchen_id": "b76d019f-5937-4a14-8091-1d9f18666c93",
        "delivery_id": "f2861560-e9ed-4463-955f-0c55c3b416fb"
    })
    if response:
        print("Order created successfully:")
        print(response)
    else:
        print("Failed to create order.")

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    create_order()