class ChatRoomManager:
    def __init__(self):
        self.rooms = {}

    def join_room(self, room_name: str, websocket):
        if room_name not in self.rooms:
            self.rooms[room_name] = []
        self.rooms[room_name].append(websocket)

    def leave_room(self, room_name: str, websocket):
        if room_name in self.rooms:
            self.rooms[room_name].remove(websocket)
            if not self.rooms[room_name]:
                del self.rooms[room_name]

    async def broadcast(self, room_name: str, message: str):
        if room_name in self.rooms:
            for websocket in self.rooms[room_name]:
                await websocket.send_text(message)

chat_rooms = ChatRoomManager()