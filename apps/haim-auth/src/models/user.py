from pydantic import BaseModel
from typing import Optional

class User(BaseModel):

    uuid: str
    username: str

class UserCreate(BaseModel):

    username: str
    password: str

class UserUpdate(BaseModel):

    username: Optional[str] = None
    password: Optional[str] = None
