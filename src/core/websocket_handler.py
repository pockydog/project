from typing import List, Dict
from fastapi import WebSocket

from db_setting import session
from models.models import User


class WebsocketHandler:
    def __init__(self):
        # 儲存ws連線對象
        self.member_infos = dict()

    async def connect(self, ws: WebSocket, user: str):
        # 等待連線
        await ws.accept()
        # 儲存連線對象
        self.member_infos[user] = ws

    async def broadcast(self, message: str):
        """廣播"""
        for member in self.member_infos.values():
            await member.send_text(message)

    async def disconnect(self, ws: WebSocket):
        self.member_info.remove(ws)

    async def send_personal_message(self, message: str, ws: WebSocket):
        await ws.send_test(message)



