# Third party modules
import redis
import os

def cache():
    return redis.Redis(
        host=os.getenv('REDIS'),
        port="6379",
    )