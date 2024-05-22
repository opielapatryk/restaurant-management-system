from repositories.mongorepo import MongoRepo
from repositories.redis import cache
from use_cases.menu_list import menu_list_use_case
from fastapi import FastAPI,status,HTTPException,Depends
import pickle

app = FastAPI(docs_url="/api/v1/display/docs",openapi_url="/api/v1/display/openapi.json")

class EntityDoesNotExist(Exception):
    """Raised when entity was not found in database."""

@app.get("/api/v1/display",
    status_code=status.HTTP_200_OK,
    name="get_menu",
)
def get_menu(redis_client: cache = Depends(cache)):
    if (cached_menu := redis_client.get("menu_1")) is not None:
        return pickle.loads(cached_menu)

    try:
        repo = MongoRepo()
        menu = menu_list_use_case(repo)
        
        redis_client.set("menu_1", pickle.dumps(menu))

        return menu

    except EntityDoesNotExist:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Menu not found!"
        )