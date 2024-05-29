# Local modules
from src.domain.dish import Dish, DishUpdate
from src.repositories.redis import RedisRepo
from src.use_cases.add_dish import add_dish
from src.use_cases.delete_cart import delete_cart
from src.use_cases.delete_dish import delete_dish
from src.use_cases.get_cart import get_cart
from src.use_cases.update_dish_qt import update_dish_qt

# Third party modules
from fastapi import FastAPI, HTTPException, Cookie, Response

# Built-in modules
import json
import uuid

app = FastAPI()
repo = RedisRepo()

@app.post("/api/v1/cart/dishes/", response_model=Dish)
async def add_dish_to_cart(dish: Dish, response: Response, session_id: str = Cookie(None)):
    if not session_id:
        session_id = str(uuid.uuid4())
        response.set_cookie(key="session_id", value=session_id)
    
    add_dish(repo,dish,session_id)

    return dish

@app.get("/api/v1/cart/dishes/")
async def get_cart_dishes(session_id: str = Cookie(None)):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID is required")

    cart_dishes = get_cart(repo,session_id)
    if not cart_dishes:
        raise HTTPException(status_code=404, detail="Cart not found")
    return {dish_id.decode(): json.loads(dish_data.decode()) for dish_id, dish_data in cart_dishes.items()}

@app.put("/api/v1/cart/dishes/{dish_id}")
async def update_dish_quantity(dish_id: str, dish_update: DishUpdate, session_id: str = Cookie(None)):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID is required")
    
    result = update_dish_qt(repo,dish_update,dish_id,session_id)
    if not result:
       raise HTTPException(status_code=404, detail=f"Dish {dish_id} not found in cart")
    
    return update_dish_qt(repo,dish_update,dish_id,session_id)

@app.delete("/api/v1/cart/dishes/{dish_id}")
async def remove_dish_from_cart(dish_id: str, session_id: str = Cookie(None)):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID is required")
    
    result = delete_dish(repo,session_id,dish_id)

    if not result:
        raise HTTPException(status_code=404, detail="dish not found in cart")
    return {"message": "dish removed"}

@app.delete("/api/v1/cart")
async def clear_cart(session_id: str = Cookie(None)):
    if not session_id:
        raise HTTPException(status_code=400, detail="Session ID is required")

    delete_cart(repo,session_id)
    return {"message": "Cart cleared"}