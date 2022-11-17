from pydantic import BaseModel
from typing import Optional, Any

class Domain(BaseModel):

    uuid: str
    name: str
    created: Optional[Any] = None
    updated: Optional[Any] = None
    deleted: Optional[Any] = None

class DomainCreate(BaseModel):

    name: str

class DomainUpdate(BaseModel):

    name: Optional[str] = None
