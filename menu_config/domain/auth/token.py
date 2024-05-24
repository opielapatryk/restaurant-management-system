# Third party modules
from pydantic import BaseModel

class TokenData(BaseModel):
    token: str