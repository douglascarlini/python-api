from fastapi_jwt import JwtAuthorizationCredentials
from fastapi import APIRouter, Security
from typing import List, Union
import os

from models.common import *
from common.security import bearer
from models.role_permission import RolePermission
from repositories.role_permission import RolePermissionRepository

router = APIRouter()

@router.post("/", tags=["role_permission"], response_model=Union[ResponseCreated, ResponseError])
async def add_role_permission(role_permission: RolePermission, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        uuid = RolePermissionRepository().create(role_permission.dict())
        return ResponseCreated(uuid=uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.delete("/{role_uuid}/{permission_uuid}", tags=["role_permission"], response_model=Union[ResponseDeleted, ResponseError])
async def del_role_permission(role_uuid: str, permission_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = RolePermissionRepository().delete({"role_uuid": role_uuid, "permission_uuid": permission_uuid})
        return ResponseDeleted(total=total)

    except Exception as e:

        return ResponseError(error=str(e))
