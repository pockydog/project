from random import choice

from fastapi import WebSocket, APIRouter
from fastapi.responses import HTMLResponse
from core.websocket_handler import WebsocketHandler

ws_router = APIRouter(prefix='/websocket')

WebsocketHandler = WebsocketHandler()


@ws_router.get('/{user}')
async def get(user: str):
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Chat</title>
        </head>
        <body>
            <h1>WebSocket Chat</h1>
            <form action="" onsubmit="sendMessage(event)">
                <input type="text" id="messageText" autocomplete="off"/>
                <button>Send</button>
            </form>
            <ul id='messages'>
            </ul>
            <script>
                var ws = new WebSocket("ws://localhost:8200/websocket/""" + user + """");
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                function sendMessage(event) {
                    var input = document.getElementById("messageText")
                    ws.send(input.value)
                    input.value = ''
                    event.preventDefault()
                }
            </script>
        </body>
    </html>
    """
    return HTMLResponse(html)


@ws_router.websocket('/{user}')
async def websocket_endpoint(websocket: WebSocket, user: str):
    await WebsocketHandler.connect(websocket, user=user)
    await WebsocketHandler.broadcast(f'你好{user}')
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"你說: {data}")
        num = choice(list(WebsocketHandler.member_infos.values()))
        await num.send_text(f"{user}說了{data}")


@ws_router.get('/talk/{user}')
async def get3(user: str):
    html = """
    <!DOCTYPE html>
    <html>
        <head>
            <title>Chat</title>
        </head>
        <body>
            <h1>WebSocket Chat</h1>
            <form action="" onsubmit="sendMessage(event)">
                <input type="text" id="messageText" autocomplete="off"/>
                <button>Send</button>
            </form>
            <ul id='messages'>
            </ul>
            <script>
                var ws = new WebSocket("ws://localhost:8200/websocket/talk/""" + user + """");
                ws.onmessage = function(event) {
                    var messages = document.getElementById('messages')
                    var message = document.createElement('li')
                    var content = document.createTextNode(event.data)
                    message.appendChild(content)
                    messages.appendChild(message)
                };
                function sendMessage(event) {
                    var input = document.getElementById("messageText")
                    ws.send(input.value)
                    input.value = ''
                    event.preventDefault()
                }
            </script>
        </body>
    </html>
    """
    return HTMLResponse(html)


@ws_router.websocket('/talk/{user}')
async def websocket_endpoint(websocket: WebSocket, user: str):
    await WebsocketHandler.connect(websocket, user=user)
    online = [w for w in WebsocketHandler.member_infos.keys()]
    await WebsocketHandler.broadcast(f'目前線上人員：{online}')
    await WebsocketHandler.broadcast('請選聊天對象')
    data = await websocket.receive_text()
    if data in WebsocketHandler.member_infos.keys():
        num = WebsocketHandler.member_infos[data]
        await websocket.send_text(f"開始與: {data}交談")
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"你說: {data}")
            await num.send_text(f"{user}說了{data}")



