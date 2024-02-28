from pydantic import BaseModel
from typing import Text, Optional

class Users(BaseModel):
    id:Optional[str]
    name:str
    email:str
    password:str

    