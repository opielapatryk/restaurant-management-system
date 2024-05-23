# Third party modules
import pika

# Local modules
from core.config import settings

class RabbitMQConsumer:
    def __init__(self, callback):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=settings.RABBITMQ_URL))
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue='task_queue', durable=True)
        self.callback = callback

    def consume(self):
        self.channel.basic_qos(prefetch_count=1)
        self.channel.basic_consume(queue='task_queue', on_message_callback=self.on_message)
        self.channel.start_consuming()

    def on_message(self, ch, method, properties, body):
        self.callback(body)
        ch.basic_ack(delivery_tag=method.delivery_tag)

    def close(self):
        self.connection.close()
