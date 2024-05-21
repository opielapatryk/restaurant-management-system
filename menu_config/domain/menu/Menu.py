import dataclasses
from typing import Optional
import uuid

@dataclasses.dataclass
class Menu:
    id: Optional[uuid.UUID] = dataclasses.field(metadata={'alias': '_id'})
    name: str
    description: str
    dishes: list
    active: bool
    
    @classmethod
    def from_dict(cls, d):
        return cls(**d)
        
    def to_dict(self):
        return dataclasses.asdict(self)
