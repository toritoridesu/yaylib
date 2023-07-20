"""
MIT License

Copyright (c) 2023-present Qvco, Konn

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import json
import websocket

from .config import Configs
from .models import Message, ChatRoom, GroupUpdateEvent
from .responses import WebSocketResponse


class WebSocket(object):
    def __init__(self):
        self.ws = None

    def _on_open(self, ws):
        pass

    def _on_message(self, ws, message):
        pass

    def _on_error(self, ws, error):
        print(error)

    def _on_close(self, ws):
        print("WebSocket closed.")

    def run(self, ws_token):
        self.ws = websocket.WebSocketApp(
            url=f"wss://{Configs.YAY_CABLE_HOST}/?token={ws_token}&app_version={Configs.YAY_VERSION_NAME}",
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close,
        )
        self.ws.run_forever()


class MessageEventListener(WebSocket):
    """Event Listener for chat messages"""

    def __init__(self, chat_room_id: int):
        super().__init__()
        self.chat_room_id = chat_room_id

    def _on_open(self, ws):
        ws.send(
            json.dumps(
                {
                    "command": "subscribe",
                    "identifier": f'{{"channel":"MessagesChannel", "chat_room_id": {self.chat_room_id}}}',
                }
            )
        )

    def _on_message(self, ws, message):
        message = json.loads(message)

        if "identifier" in message and "type" not in message:
            message = WebSocketResponse(message).message["data"]
            self.on_message(Message(message))

    def on_message(self, message: Message):
        pass


class ChatEventListener(WebSocket):
    """Event Listener for ChatRoom"""

    def __init__(self):
        super().__init__()

    def _on_open(self, ws):
        ws.send(
            json.dumps(
                {
                    "command": "subscribe",
                    "identifier": '{"channel":"ChatRoomChannel"}',
                }
            )
        )

    def _on_message(self, ws, message):
        message = json.loads(message)

        if "identifier" in message and "type" not in message:
            message = WebSocketResponse(message).message

            if "event" not in message:
                self.on_message(ChatRoom(message.get("chat")))
            elif message.get("event") == "chat_deleted":
                self.on_delete(message.get("data").get("room_id"))

    def on_message(self, chat_room: ChatRoom):
        pass

    def on_delete(self, room_id: int):
        pass


class GroupEventListener(WebSocket):
    """Event Listener for all the group updates on Yay!"""

    def __init__(self):
        super().__init__()

    def _on_open(self, ws):
        ws.send(
            json.dumps(
                {
                    "command": "subscribe",
                    "identifier": '{"channel":"GroupUpdatesChannel"}',
                }
            )
        )

    def _on_message(self, ws, message):
        message = json.loads(message)

        if "identifier" in message and "type" not in message:
            message = GroupUpdateEvent(WebSocketResponse(message).message)
            if message.event == "new_post":
                self.on_post(message.group_id)

    def on_post(self, group_id: int):
        pass


class GroupPostEventListener(WebSocket):
    """Event Listener for group posts"""

    def __init__(self, group_id: int):
        super().__init__()
        self.group_id = group_id

    def _on_open(self, ws):
        ws.send(
            json.dumps(
                {
                    "command": "subscribe",
                    "identifier": f'{{"channel":"GroupPostsChannel", "group_id": {self.group_id}}}',
                }
            )
        )

    def _on_message(self, ws, message):
        message = json.loads(message)

        if "identifier" in message and "type" not in message:
            message = GroupUpdateEvent(WebSocketResponse(message).message)
            if message.event == "new_post":
                self.on_post(message.group_id)

    def on_post(self, group_id: int):
        pass
