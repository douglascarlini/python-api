from pydantic import BaseModel
from typing import Optional

class User(BaseModel):

    role_uuid: str
    username: str
    name: str
    uuid: str

class UserCreate(BaseModel):

    role_uuid: str
    username: str
    password: str
    name: str

class UserUpdate(BaseModel):

    role_uuid: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    name: Optional[str] = None