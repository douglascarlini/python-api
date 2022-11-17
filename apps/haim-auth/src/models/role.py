from pydantic import BaseModel
from typing import Optional, Any

class Role(BaseModel):

    uuid: str
    name: str
    identifier: str
    domain_uuid: str
    created: Optional[Any] = None
    updated: Optional[Any] = None
    deleted: Optional[Any] = None

class RoleCreate(BaseModel):

    name: str
    identifier: str
    domain_uuid: str

class RoleUpdate(BaseModel):

    name: Optional[str] = None
    identifier: Optional[str] = None
    domain_uuid: Optional[str] = None
