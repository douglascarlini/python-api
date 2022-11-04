from pydantic import BaseModel
from typing import Optional

class Auth(BaseModel):

    username: str
    password: str

class AuthPayload(BaseModel):

    username: str
    role: str
    name: str
    uuid: str

class AuthToken(BaseModel):

    token: str