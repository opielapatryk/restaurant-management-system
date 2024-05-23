# Third party modules
import pymongo

# Built-in modules
import json
import os

class MongoRepo:
    def __init__(self, json_file_name='example_menu.json'):
        client = pymongo.MongoClient("mongodb://root:mongodb@localhost:27017")

        self.db = client['menu_display']
        self.collection = self.db.menu

        base_path = os.path.dirname(__file__)
        json_file_path = os.path.join(base_path, json_file_name)
        
        # Check if collection is empty, then insert initial data
        if self.collection.count_documents({}) == 0:
            self.insert_initial_data(json_file_path)

    def insert_initial_data(self, json_file_path):
        with open(json_file_path, 'r') as file:
            menu_data = json.load(file)
            self.collection.insert_one(menu_data)

    def _create_menu_object(self, menu_data):
        return {
            "_id": str(menu_data["_id"]),
            "name": menu_data["name"],
            "description": menu_data["description"],
            "dishes": menu_data["dishes"],
            "active": menu_data["active"]
        }

    def list(self):
        result = self.collection.find_one()
        menu = self._create_menu_object(result)
        return menu