import pymongo

class MongoRepo:
    def __init__(self):
        client = pymongo.MongoClient(
            host='localhost',
            port=27017,
            username='root',
            password='mongodb',
        )

        self.db = client['menu_display']

    def _create_menu_object(self, menu_data):
        return {
            "_id": str(menu_data["_id"]),
            "name": menu_data["name"],
            "description": menu_data["description"],
            "dishes": menu_data["dishes"],
        }

    def list(self):
        collection = self.db.menu
        result = collection.find_one()
        menu = self._create_menu_object(result)
        return menu