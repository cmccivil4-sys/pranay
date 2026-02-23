from fastapi import APIRouter, WebSocket

router = APIRouter(prefix='/lab', tags=['lab'])


@router.websocket('/ws/{room_id}')
async def lab_ws(socket: WebSocket, room_id: str) -> None:
    await socket.accept()
    await socket.send_json({'event': 'connected', 'room_id': room_id})
    while True:
        data = await socket.receive_text()
        await socket.send_json({'event': 'sync', 'room_id': room_id, 'payload': data})
