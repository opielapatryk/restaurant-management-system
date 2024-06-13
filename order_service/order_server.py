import grpc
from concurrent import futures
import logging
from google.protobuf.timestamp_pb2 import Timestamp
import order_pb2
import order_pb2_grpc
from src.gRPC.db import MongoRepo

class OrderService(order_pb2_grpc.OrderServiceServicer):
    def __init__(self):
        self.repo = MongoRepo()

    def CreateOrder(self, request, context):
        try:
            # Convert the request to a dictionary
            order_dict = {
                "_id": request.id,  # Ensure this is a valid unique identifier
                "items": [{"product": item.product, "quantity": item.quantity} for item in request.items],
                "status": request.status,
                "created": request.created.ToDatetime(),  # Convert Timestamp to datetime
                "customer_id": request.customer_id,
                "kitchen_id": request.kitchen_id,
                "delivery_id": request.delivery_id
            }
            logging.info(f"Inserting order: {order_dict}")  # Add logging to inspect the order
            self.repo.insert_order(order_dict)
            return request
        except Exception as e:
            logging.error(f"Failed to insert order: {e}")
            context.set_details(str(e))
            context.set_code(grpc.StatusCode.INTERNAL)
            return order_pb2.Order()

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    order_pb2_grpc.add_OrderServiceServicer_to_server(OrderService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    logging.info("Server started. Listening on port 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    serve()
