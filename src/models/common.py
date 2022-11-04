from pydantic import BaseModel
from typing import Optional

class ResponseCreated(BaseModel):

    uuid: str

class ResponseUpdated(BaseModel):

    total: int

class ResponseDeleted(BaseModel):

    total: int

class ResponseError(BaseModel):

    error: str

class Paginate(BaseModel):

    page: int
    rows: int

class Search(BaseModel):

    where: Optional[dict] = None
    pager: Optional[Paginate] = Paginate(page=0, rows=100)

