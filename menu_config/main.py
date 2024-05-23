# Local modules
from repositories.mongorepo import MongoRepo
from use_cases.menu_list import menu_list_use_case
from use_cases.menu_get import menu_get_use_case
from use_cases.menu_post import menu_post_use_case
from use_cases.menu_put import menu_put_use_case
from use_cases.menu_patch import menu_patch_use_case
from use_cases.menu_delete import menu_delete_use_case
from use_cases.producer import ProducerService
from repositories.rabbitmq import RabbitMQProducer

# Third party modules
from fastapi import FastAPI,status,HTTPException

# Built-in modules
import json

app = FastAPI(docs_url="/api/v1/config/docs",openapi_url="/api/v1/config/openapi.json")

def produce_message(message,service: ProducerService = ProducerService, broker: RabbitMQProducer = RabbitMQProducer):
    try:
        service(broker).send_message(message)
        return {"status": "Message sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class EntityDoesNotExist(Exception):
    """Raised when entity was not found in database."""

@app.get("/api/v1/config",
    status_code=status.HTTP_200_OK,
    name="get_menu",
)
def get_menu():
    try:
        repo = MongoRepo()
        menu = menu_list_use_case(repo)

        return menu

    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found!"
        )
    
@app.get("/api/v1/config/{id}",
    status_code=status.HTTP_200_OK,
    name="get_menu",
)
def get_menu_by_id(id):
    try:
        repo = MongoRepo()
        menu = menu_get_use_case(repo, id)
        
        return menu

    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found!"
        )
    
@app.post("/api/v1/config/",
    status_code=status.HTTP_201_CREATED,
    name="post_menu",
)
def post_menu(menu: dict):
    repo = MongoRepo()

    try:
      result = menu_post_use_case(repo, menu)
      
      if menu.get('active') == True:
        produce_message(result)
      
      return result
    except:
      raise HTTPException(status_code=400, detail="Menu already exists or missing required fields")
    
@app.put("/api/v1/config/{id}",
    status_code=status.HTTP_201_CREATED,
    name="put_menu",
)
def put_menu(menu: dict,id):
    repo = MongoRepo()

    name = menu.get('name')
    description = menu.get('description')
    dishes = menu.get('dishes')
    active = menu.get('active')

    if not name or not description or not dishes or not active:
        raise HTTPException(status_code=400, detail="Missing required fields")

    try:
      result = menu_put_use_case(repo, menu, id)

      return result
    except:
      raise HTTPException(status_code=400, detail="Failed to update menu")
    
@app.patch("/api/v1/config/{id}",
    status_code=status.HTTP_200_OK,
    name="patch_menu",
)
def patch_menu(menu: dict,id):
    repo = MongoRepo()

    try:
      result = menu_patch_use_case(repo, menu, id)
      
      return result
    except:
      raise HTTPException(status_code=400, detail="Failed to update menu")
    
@app.delete("/api/v1/config/{id}",
    status_code=status.HTTP_200_OK,
    name="delete_menu",
)
def delete_menu(id):
    repo = MongoRepo()

    try:
      result = menu_delete_use_case(repo, id)
      return result
    except:
      raise HTTPException(status_code=400, detail="Failed to delete menu")
    