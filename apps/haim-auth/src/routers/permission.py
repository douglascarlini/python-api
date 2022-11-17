from fastapi_jwt import JwtAuthorizationCredentials
from fastapi import APIRouter, Security
from typing import List, Union
import os

from models.common import *
from common.security import bearer
from repositories.permission import PermissionRepository
from models.permission import Permission, PermissionCreate, PermissionUpdate

router = APIRouter()

@router.get("/{permission_uuid}", tags=["permissions"], response_model=Union[None, Permission, ResponseError])
async def get_permission(permission_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        return PermissionRepository().getByUUID(permission_uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.patch("/", tags=["permissions"], response_model=Union[List[Permission], ResponseError])
async def get_permission_list(search: Search, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        return PermissionRepository().search(search.where, pager=search.pager.dict())

    except Exception as e:

        return ResponseError(error=str(e))

@router.post("/", tags=["permissions"], response_model=Union[ResponseCreated, ResponseError])
async def add_permission(permission: PermissionCreate, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        uuid = PermissionRepository().create(permission.dict())
        return ResponseCreated(uuid=uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.put("/{permission_uuid}", tags=["permissions"], response_model=Union[ResponseUpdated, ResponseError])
async def set_permission(permission_uuid: str, permission: PermissionUpdate, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = PermissionRepository().update(permission.dict(), {"uuid": permission_uuid})
        return ResponseUpdated(total=total)

    except Exception as e:

        return ResponseError(error=str(e))

@router.delete("/{permission_uuid}", tags=["permissions"], response_model=Union[ResponseDeleted, ResponseError])
async def del_permission(permission_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = PermissionRepository().delete({"uuid": permission_uuid})
        return ResponseDeleted(total=total)

    except Exception as e:

        return ResponseError(error=str(e))
