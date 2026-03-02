from fastapi import WebSocket


class ConnectionManager:
    def __init__(self):
        self.connections: list[WebSocket] = []

    async def connect(self, ws: WebSocket):
        await ws.accept()
        self.connections.append(ws)

    def disconnect(self, ws: WebSocket):
        if ws in self.connections:
            self.connections.remove(ws)

    async def broadcast(self, event: str, payload: dict):
        data = {"event": event, "data": payload}
        for conn in list(self.connections):
            try:
                await conn.send_json(data)
            except Exception:
                self.disconnect(conn)


manager = ConnectionManager()
