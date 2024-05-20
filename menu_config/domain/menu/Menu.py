import dataclasses

@dataclasses.dataclass
class Menu:
    id: int
    name: str
    description: str
    dishes: list
    active: bool
    
    @classmethod
    def from_dict(self,d):
        return self(**d)
        
    def to_dict(self):
        return dataclasses.asdict(self)