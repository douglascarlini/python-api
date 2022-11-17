from pydantic import BaseModel
from typing import Optional, Any

class Permission(BaseModel):

    uuid: str
    name: str
    description: str
    created: Optional[Any] = None
    updated: Optional[Any] = None
    deleted: Optional[Any] = None

class PermissionCreate(BaseModel):

    name: str
    config: str
    description: str

class PermissionUpdate(BaseModel):

    name: Optional[str] = None
    config: Optional[str] = None
    description: Optional[str] = None
