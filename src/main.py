# DO NOT NEEDED IF RUNNING ON DOCKER
from dotenv import load_dotenv
load_dotenv()

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import os

from routers import auth, domain, permission, role, user, user_role, role_permission
from common import ws

# APP CONFIG
app = FastAPI(title=os.getenv("APP_NAME"), description=os.getenv("APP_DESC"), version=os.getenv("APP_VERSION"))

# ADD CORS
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# WEBSOCKET
ws.Server.init(app)

# ROUTERS
app.include_router(auth.router, prefix="/auth")
app.include_router(permission.router, prefix="/permissions")
app.include_router(domain.router, prefix="/domains")
app.include_router(role.router, prefix="/roles")
app.include_router(user.router, prefix="/users")
app.include_router(role_permission.router, prefix="/role_permission")
app.include_router(user_role.router, prefix="/user_role")

# START SERVER
uvicorn.run(app, host="0.0.0.0", port=80)
