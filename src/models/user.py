from pydantic import BaseModel
from typing import Optional

class User(BaseModel):

    uuid: str
    name: str
    username: str
    role_uuid: str

class UserCreate(BaseModel):

    name: str
    username: str
    password: str
    role_uuid: str

class UserUpdate(BaseModel):

    name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    role_uuid: Optional[str] = None