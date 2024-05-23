# Local modules
from repositories.mongorepo import MongoRepo
from repositories.redis import cache
from use_cases.menu_list import menu_list_use_case
from use_cases.consumer import ConsumerService
from repositories.rabbitmq import RabbitMQConsumer

# Third party modules
from fastapi import FastAPI,status,HTTPException,Depends
import pickle

# Built-in modules
from threading import Thread

def start_consumer(service: ConsumerService = ConsumerService, broker: RabbitMQConsumer = RabbitMQConsumer):
    thread = Thread(target=service(broker).start_consuming)
    thread.start()
    return {"status": "Consumer started"}

start_consumer()

app = FastAPI(docs_url="/api/v1/display/docs",openapi_url="/api/v1/display/openapi.json")

class EntityDoesNotExist(Exception):
    """Raised when entity was not found in database."""

@app.get("/api/v1/display",
    status_code=status.HTTP_200_OK,
    name="get_menu",
)
def get_menu(redis_client: cache = Depends(cache)):
    if (cached_menu := redis_client.get("menu")) is not None:
        return pickle.loads(cached_menu)

    try:
        repo = MongoRepo()
        menu = menu_list_use_case(repo)
        
        redis_client.set("menu", pickle.dumps(menu))

        return menu

    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found!"
        )