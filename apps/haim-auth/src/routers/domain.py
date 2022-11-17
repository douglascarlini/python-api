from fastapi_jwt import JwtAuthorizationCredentials
from fastapi import APIRouter, Security
from typing import List, Union
import os

from models.common import *
from common.security import bearer
from repositories.domain import DomainRepository
from models.domain import Domain, DomainCreate, DomainUpdate

router = APIRouter()

@router.get("/{domain_uuid}", tags=["domains"], response_model=Union[None, Domain, ResponseError])
async def get_domain(domain_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        return DomainRepository().getByUUID(domain_uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.patch("/", tags=["domains"], response_model=Union[List[Domain], ResponseError])
async def get_domain_list(search: Search, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        data = DomainRepository().search(search.where, pager=search.pager.dict())

        print(data)

        return data

    except Exception as e:

        return ResponseError(error=str(e))

@router.post("/", tags=["domains"], response_model=Union[ResponseCreated, ResponseError])
async def add_domain(domain: DomainCreate, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        uuid = DomainRepository().create(domain.dict())
        return ResponseCreated(uuid=uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.put("/{domain_uuid}", tags=["domains"], response_model=Union[ResponseUpdated, ResponseError])
async def set_domain(domain_uuid: str, domain: DomainUpdate, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = DomainRepository().update(domain.dict(), {"uuid": domain_uuid})
        return ResponseUpdated(total=total)

    except Exception as e:

        return ResponseError(error=str(e))

@router.delete("/{domain_uuid}", tags=["domains"], response_model=Union[ResponseDeleted, ResponseError])
async def del_domain(domain_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = DomainRepository().delete({"uuid": domain_uuid})
        return ResponseDeleted(total=total)

    except Exception as e:

        return ResponseError(error=str(e))
