# Third party modules
import redis

# Built-in modules
import json
import os

class RedisRepo():
    def __init__(self):
        self.cache = redis.Redis(
            host=os.getenv('REDIS_HOST','localhost'),
            port="6379",
        )

    def post(self,dish,session_id):
        cart_key = f"cart:{session_id}"
        self.cache.hset(cart_key, dish.dish_id, dish.quantity)

    def delete_cart(self,session_id):
        cart_key = f"cart:{session_id}"
        self.cache.delete(cart_key)

    def delete_dish(self,session_id, dish_id):
        cart_key = f"cart:{session_id}"
        return self.cache.hdel(cart_key, dish_id)

    def list(self,session_id):
        cart_key = f"cart:{session_id}"
        return self.cache.hgetall(cart_key)
    
    def put(self,updated_dish,dish_id,session_id):
        cart_key = f"cart:{session_id}"
        if not self.cache.hexists(cart_key, dish_id):
            return False
        
        updated_dish = {"dish_id": dish_id, "quantity": updated_dish.quantity}
        self.cache.hset(cart_key, dish_id, json.dumps(updated_dish))
        return updated_dish