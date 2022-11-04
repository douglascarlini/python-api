from fastapi import WebSocket, Depends, Query, WebSocketDisconnect
from fastapi_jwt_auth import AuthJWT
import json

class Manager:

    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, data):
        message = json.dumps(data)
        for connection in self.active_connections:
            await connection.send_text(message)

manager = Manager()

class Server(object):

    @staticmethod
    def init(app):

        @app.websocket("/ws")
        async def websocket(websocket: WebSocket, token: str = Query(...), Authorize: AuthJWT = Depends()):

            try:

                Authorize.jwt_required("websocket", token=token)
                decoded = Authorize.get_raw_jwt(token)
                await manager.connect(websocket)
                subject = decoded['subject']

                await manager.broadcast(f"Client #{subject['username']} join")

                while True:

                    data = await websocket.receive_text()
                    await manager.broadcast(f"Client #{subject['username']}: {data}")

            except WebSocketDisconnect:

                manager.disconnect(websocket)
                await manager.broadcast(f"Client #{subject['username']} left")

            except Exception as e:

                print(str(e))