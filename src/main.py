# DO NOT NEEDED IF RUNNING ON DOCKER
from dotenv import load_dotenv
load_dotenv()

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
import os

from routers import root, auth, role, user
from common import ws

# APP CONFIG
app = FastAPI(title=os.getenv('APP_NAME'), description=os.getenv('APP_DESC'), version=os.getenv('APP_VERSION'))

# ADD CORS
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

# ROUTERS
app.include_router(root.router, prefix="/root")
app.include_router(auth.router, prefix="/auth")
app.include_router(role.router, prefix="/roles")
app.include_router(user.router, prefix="/users")

# WEBSOCKET
ws.Server.init(app)

# START SERVER
uvicorn.run(app, host="0.0.0.0", port=int(os.getenv('APP_PORT')))