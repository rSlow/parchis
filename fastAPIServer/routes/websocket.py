from fastapi import APIRouter, Path
from fastapi import WebSocket, WebSocketDisconnect

from game.game_server import GameServer

websocket_router = APIRouter(
    prefix="/ws",
    tags=["WS"]

)

game = GameServer()


@websocket_router.websocket("/rooms/")
async def websocket_endpoint(websocket: WebSocket):
    await game.register_socket(websocket)
    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        await game.disconnect_socket(websocket)
