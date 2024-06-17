# Third party modules
import redis
import os

def cache():
    return redis.Redis(
        host=os.getenv('REDIS','localhost'),
        port="6379",
    )