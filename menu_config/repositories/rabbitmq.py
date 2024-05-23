# Third party modules 
import pika

# Local modules
from core.config import settings

class RabbitMQProducer:
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_URL))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='task_queue', durable=True)

    def publish(self, message: str):
        self.channel.basic_publish(
            exchange='',
            routing_key='task_queue',
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )

    def close(self):
        self.connection.close()
