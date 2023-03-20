from fastapi import APIRouter, Query, Path
from fastapi import WebSocket, WebSocketDisconnect

from game.game_server import GameServer

websocket_router = APIRouter(
    prefix="/ws",
    tags=["WS"]

)

server = GameServer()


@websocket_router.websocket("/rooms/")
async def websocket_rooms_endpoint(websocket: WebSocket, user_id: int = Query(default=None)):
    await server.main_sockets.register(websocket)
    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        await server.main_sockets.disconnect(websocket)


@websocket_router.websocket("/rooms/{room_id}")
async def websocket_room_endpoint(websocket: WebSocket, room_id: int = Path(), user_id: int = Query(default=None)):
    await server.room_sockets.register(websocket, room_id)
    try:
        while True:
            await websocket.receive_text()

    except WebSocketDisconnect:
        await server.room_sockets.disconnect(websocket, room_id)
