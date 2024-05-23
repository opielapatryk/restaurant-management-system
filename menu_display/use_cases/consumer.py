class ConsumerService:
    def __init__(self, broker):
        self.consumer = broker(self.process_message)

    def process_message(self, message: bytes):
        print(f"Received message: {message.decode('utf-8')}")

    def start_consuming(self):
        self.consumer.consume()
