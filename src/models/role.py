from pydantic import BaseModel
from typing import Optional

class Role(BaseModel):

    uuid: str
    name: str

class RoleCreate(BaseModel):

    name: str

class RoleUpdate(BaseModel):

    name: str
