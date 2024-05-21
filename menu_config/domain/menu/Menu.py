import dataclasses

@dataclasses.dataclass
class Menu:
    _id: str
    name: str
    description: str
    dishes: list
    active: bool
    
    @classmethod
    def from_dict(cls, d):
        return cls(**d)
        
    def to_dict(self):
        return dataclasses.asdict(self)
