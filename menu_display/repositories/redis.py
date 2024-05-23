# Third party modules
import redis

def cache():
    return redis.Redis(
        host="127.0.0.1",
        port="6379",
    )