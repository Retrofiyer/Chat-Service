from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from app.rooms import chat_rooms

app = FastAPI()

@app.websocket("/ws/{room_name}/{username}")
async def websocket_endpoint(websocket: WebSocket, room_name: str, username: str):
    await websocket.accept()
    chat_rooms.join_room(room_name, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            message = f"{username}: {data}"
            await chat_rooms.broadcast(room_name, message)
    except WebSocketDisconnect:
        chat_rooms.leave_room(room_name, websocket)
        leave_message = f"{username} left the chat"
        await chat_rooms.broadcast(room_name, leave_message)