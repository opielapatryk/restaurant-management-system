# Built-in modules
import dataclasses

@dataclasses.dataclass
class Dish:
    id: int
    name: str
    description: str
    availabilityQty: int
    price: float
    category: str
    ingredients: list
    active: bool
    image: str
    dietaryrestrictions: list
    
    @classmethod
    def from_dict(self,d):
        return self(**d)
    
    def to_dict(self):
        return dataclasses.asdict(self)
    