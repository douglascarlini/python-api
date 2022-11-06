from fastapi_jwt import JwtAuthorizationCredentials
from fastapi import APIRouter, Security
from typing import List, Union
import os

from models.common import *
from common.security import bearer
from repositories.role import RoleRepository
from models.role import Role, RoleCreate, RoleUpdate

router = APIRouter()

@router.get("/{role_uuid}", tags=["roles"], response_model=Union[None, Role, ResponseError])
async def get_role(role_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        return RoleRepository().getByUUID(role_uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.patch("/", tags=["roles"], response_model=Union[List[Role], ResponseError])
async def get_role_list(search: Search, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        return RoleRepository().search(search.where, pager=search.pager.dict())

    except Exception as e:

        return ResponseError(error=str(e))

@router.post("/", tags=["roles"], response_model=Union[ResponseCreated, ResponseError])
async def add_role(role: RoleCreate, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        uuid = RoleRepository().create(role.dict())
        return ResponseCreated(uuid=uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.put("/{role_uuid}", tags=["roles"], response_model=Union[ResponseUpdated, ResponseError])
async def set_role(role_uuid: str, role: RoleUpdate, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = RoleRepository().update(role.dict(), {'uuid': role_uuid})
        return ResponseUpdated(total=total)

    except Exception as e:

        return ResponseError(error=str(e))

@router.delete("/{role_uuid}", tags=["roles"], response_model=Union[ResponseDeleted, ResponseError])
async def del_role(role_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = RoleRepository().delete({'uuid': role_uuid})
        return ResponseDeleted(total=total)

    except Exception as e:

        return ResponseError(error=str(e))
