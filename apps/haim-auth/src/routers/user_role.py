from fastapi_jwt import JwtAuthorizationCredentials
from fastapi import APIRouter, Security
from typing import List, Union
import os

from models.common import *
from common.security import bearer
from models.user_role import UserRole
from repositories.user_role import UserRoleRepository

router = APIRouter()

@router.post("/", tags=["user_role"], response_model=Union[ResponseCreated, ResponseError])
async def add_user_role(user_role: UserRole, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        uuid = UserRoleRepository().create(user_role.dict())
        return ResponseCreated(uuid=uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.delete("/{user_uuid}/{role_uuid}", tags=["user_role"], response_model=Union[ResponseDeleted, ResponseError])
async def del_user_role(user_uuid: str, role_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = UserRoleRepository().delete({"user_uuid": user_uuid, "role_uuid": role_uuid})
        return ResponseDeleted(total=total)

    except Exception as e:

        return ResponseError(error=str(e))
