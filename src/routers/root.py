from typing import List, Union
from fastapi import APIRouter

from repositories.role import RoleRepository
from repositories.user import UserRepository
from models.common import *

router = APIRouter()

@router.post("/", tags=["root"], response_model=Union[ResponseCreated, ResponseError])
async def add_root():

    try:

        uuid = RoleRepository().create({"name": "root"})

        uuid = UserRepository().create({
            "name": "Administrator",
            "password": "123456",
            "username": "root",
            "role_uuid": uuid
        })

        return ResponseCreated(uuid=uuid)

    except Exception as e:

        return ResponseError(error=str(e))