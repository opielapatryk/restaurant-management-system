from repositories.mongorepo import MongoRepo
from repositories.redis import cache
from use_cases.menu_list import menu_list_use_case
from fastapi import FastAPI,status,HTTPException,Depends
import pickle

app = FastAPI()

class EntityDoesNotExist(Exception):
    """Raised when entity was not found in database."""

@app.get("/")
def welcome():
    return {"message": "Welcome to the Restaurant API!", "endpoints": {"menu": "api/v1/menu"}}

@app.get("/api/v1/menu",
    status_code=status.HTTP_200_OK,
    name="get_menu",
)
def get_menu(name:str=None,redis_client: cache = Depends(cache)):
    if (cached_menu := redis_client.get(f"menu_1")) is not None:
        return pickle.loads(cached_menu)

    try:
        repo = MongoRepo()
        menu = menu_list_use_case(repo)

        if name:
            menu = filter(lambda m: m['name'] == name, menu)
        
        redis_client.set(f"menu_1", pickle.dumps(menu))

        return menu

    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found!"
        )