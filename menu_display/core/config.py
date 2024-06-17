import os

class Settings:
    RABBITMQ_URL: str = os.getenv('RABBITMQ_HOST','localhost')

settings = Settings()
