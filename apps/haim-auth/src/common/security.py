from fastapi_jwt import JwtAccessBearer
from fastapi_jwt_auth import AuthJWT
from pydantic import BaseModel
from datetime import timedelta
import os

class Settings(BaseModel):

    authjwt_algorithm: str = "HS256"
    authjwt_secret_key: str = os.getenv('JWT_SECRET')

@AuthJWT.load_config
def get_config(): return Settings()

bearer = JwtAccessBearer(algorithm="HS256", secret_key=os.getenv('JWT_SECRET'), access_expires_delta=timedelta(hours=int(os.getenv('JWT_EXPIRE')) or 24), auto_error=True)
