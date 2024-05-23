class ProducerService:
    def __init__(self, broker):
        self.producer = broker()

    def send_message(self, message):
        self.producer.publish(message)
        self.producer.close()