from fastapi_jwt import JwtAuthorizationCredentials
from fastapi import APIRouter, Security
from typing import List, Union
import os

from models.common import *
from common.security import bearer
from repositories.user import UserRepository
from models.user import User, UserCreate, UserUpdate

router = APIRouter()

@router.get("/{user_uuid}", tags=["users"], response_model=Union[None, User, ResponseError])
async def get_user(user_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        return UserRepository().getByUUID(user_uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.patch("/", tags=["users"], response_model=Union[List[User], ResponseError])
async def get_user_list(search: Search, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        return UserRepository().search(search.where, pager=search.pager.dict())

    except Exception as e:

        return ResponseError(error=str(e))

@router.post("/", tags=["users"], response_model=Union[ResponseCreated, ResponseError])
async def add_user(user: UserCreate):

    try:

        uuid = UserRepository().create(user.dict())
        return ResponseCreated(uuid=uuid)

    except Exception as e:

        return ResponseError(error=str(e))

@router.put("/{user_uuid}", tags=["users"], response_model=Union[ResponseUpdated, ResponseError])
async def set_user(user_uuid: str, user: UserUpdate, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = UserRepository().update(user.dict(), {"uuid": user_uuid})
        return ResponseUpdated(total=total)

    except Exception as e:

        return ResponseError(error=str(e))

@router.delete("/{user_uuid}", tags=["users"], response_model=Union[ResponseDeleted, ResponseError])
async def del_user(user_uuid: str, credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        total = UserRepository().delete({"uuid": user_uuid})
        return ResponseDeleted(total=total)

    except Exception as e:

        return ResponseError(error=str(e))