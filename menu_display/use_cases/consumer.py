# Local modules
from repositories.mongorepo import MongoRepo
from repositories.redis import cache
from use_cases.menu_patch import menu_patch_use_case
from use_cases.menu_list import menu_list_use_case

# Built-in modules
import json

# Third party modules 
import pickle

class ConsumerService:
    def __init__(self, broker):
        self.consumer = broker(self.process_message)

    def process_message(self, message: bytes):
        repo = MongoRepo()
        current_menu_id = menu_list_use_case(repo)['_id']

        new_menu_json = json.loads(message)

        new_menu = menu_patch_use_case(repo,{'name':new_menu_json['name'],'description':new_menu_json['description'],'dishes':new_menu_json['dishes'],'active':new_menu_json['active']},current_menu_id)

        cache().set('menu', pickle.dumps(new_menu))

    def start_consuming(self):
        self.consumer.consume()
