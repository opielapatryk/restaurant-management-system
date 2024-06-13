# Third party modules
import pymongo

# Built-in modules
import os

class MongoRepo:
    def __init__(self):
        self.client = pymongo.MongoClient(f"mongodb://root:mongodb@{os.getenv('MONGO_HOST','localhost')}:27017")
        self.db_name = os.getenv('DB_NAME', 'api_db')
        # self.db = client['order_service']
        # self.collection = self.db.orders

        self.db = self.client[self.db_name]
        self.orders_collection = self.db['orders']  # Correctly initialize the orders_collection attribute


    def insert_order(self, order):
        result = self.orders_collection.insert_one(order)
        return str(result.inserted_id)

    def get_orders(self):
        return list(self.orders_collection.find())

    def get_order_by_id(self, order_id):
        return self.orders_collection.find_one({"id": order_id})

    def delete_order(self, order_id):
        return self.orders_collection.delete_one({"id": order_id})

    def update_order(self, order_id, update_data):
        return self.orders_collection.update_one({"id": order_id}, {"$set": update_data})