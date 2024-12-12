import pika

from loguru import logger

from app.queue.queue_abc import QueueABC


class RabbitMQQueue(QueueABC):

    def __init__(self, queue_name: str, host: str):
        self.queue_name = queue_name
        credentials = pika.PlainCredentials('guest', 'guest')
        parameters = pika.ConnectionParameters(host=host, port=5672, credentials=credentials)
        self.connection = pika.BlockingConnection(parameters)
        self.channel = self.connection.channel()

    def put(self, data: str):
        self.channel.basic_publish(
           exchange='',
           routing_key=self.queue_name,
           body=data.encode(),
           properties=pika.BasicProperties(
               delivery_mode=2,  # make message persistent
           )
        )

    def get(self) -> str | None:
        try:
            method_frame, _, body = self.channel.basic_get(queue=self.queue_name, auto_ack=True)
            if not method_frame:
                return None

            return body.decode()
        except Exception as e:
            logger.error(f"RabbitMQQueue error {e}")
            return None
