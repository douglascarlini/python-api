from pydantic import BaseModel
from typing import Optional

class UserRole(BaseModel):

    user_uuid: str
    role_uuid: str
