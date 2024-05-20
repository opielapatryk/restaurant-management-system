from repositories.mongorepo import MongoRepo
from use_cases.menu_list import menu_list_use_case
from use_cases.menu_get import menu_get_use_case
from fastapi import FastAPI,status,HTTPException
from fastapi.responses import RedirectResponse

app = FastAPI()

class EntityDoesNotExist(Exception):
    """Raised when entity was not found in database."""

@app.get("/", include_in_schema=False)
async def welcome():
    return RedirectResponse("/docs")

@app.get("/api/v1/menu",
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
    
@app.get("/api/v1/menu/{id}",
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
    
