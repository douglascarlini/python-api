from fastapi_jwt import JwtAuthorizationCredentials
from fastapi import APIRouter, Security
from typing import List, Union
import bcrypt

from models.auth import Auth, AuthPayload, AuthToken
from repositories.role import RoleRepository
from repositories.user import UserRepository
from common.security import bearer
from models.common import *

router = APIRouter()

@router.post("/", tags=["auth"], response_model=Union[AuthToken, ResponseError])
async def auth(auth: Auth):

    try:

        user = UserRepository().getByUsername(auth.username)
        subj = None

        if user:

            salt = user['salt'].encode('utf-8')
            check = user['password'].encode('utf-8')
            password = auth.password.encode('utf-8')

            role = RoleRepository().getByUUID(user["role_uuid"])

            if bcrypt.hashpw(password, salt) == check:

                user["role"] = role["name"]
                del user['role_uuid']
                del user['password']
                del user['created']
                del user['salt']

                subj = user

        if subj: token = bearer.create_access_token(subject=subj)
        return AuthToken(token=token if subj is not None else "")

    except Exception as e:

        return ResponseError(error=str(e))

@router.get("/me", tags=["auth"], response_model=Union[AuthPayload, ResponseError])
def me(credentials: JwtAuthorizationCredentials = Security(bearer)):

    try:

        return credentials.subject

    except Exception as e:

        return ResponseError(error=str(e))