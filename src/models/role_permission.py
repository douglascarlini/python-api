from pydantic import BaseModel
from typing import Optional

class RolePermission(BaseModel):

    role_uuid: str
    permission_uuid: str
