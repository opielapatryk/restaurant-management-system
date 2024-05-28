# Third party modules
from pydantic import BaseModel, Field

class Dish(BaseModel):
    dish_id: str
    quantity: int

class DishUpdate(BaseModel):
    dish_id: str
    quantity: int = Field(..., gt=0, description="Quantity must be greater than 0")
    