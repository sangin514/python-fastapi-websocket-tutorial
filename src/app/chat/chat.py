import asyncio
from fastapi import WebSocket
import asyncio


class Chat:
    members: dict[str, WebSocket]

    """Represents the chatting room."""

    def __init__(self):
        self.members = {}
        self.illegal_ids = ["system"]

    async def join(self, user: str, websocket: WebSocket):
        """Connect to the user and add user to the members on success."""

        # TODO Establish connection
        await websocket.accept()
        close_reason = ""

        ######### [ TODO ] #########
        # TODO Close connection on duplicate and exit method.
        ############################
        if user in self.members.keys():
            close_reason = "User {} already exists".format(user)
            await websocket.close(reason=close_reason)
        elif user in self.illegal_ids:
            close_reason = "Cannot use Username {}".format(user)
            await websocket.close(reason=close_reason)
        ######### [ TODO ] #########
        # TODO Otherwise, add user to the members.
        ############################
        else:
            self.members[user] = websocket
            json = {
                "from": "system",
                "msg": "User {} joined the chat".format(user)
            }
            await self.broadcast(json)

    async def leave(self, user: str):
        """Remove user from the members."""

        ######### [ TODO ] #########
        # TODO Remove user from the members.
        ############################
        del self.members[user]

        ######### [ TODO ] #########
        # TODO Optionally, broadcast the system message that the user left the chat.
        ############################
        json = {
            "from": "system",
            "msg": "User {} left the chat".format(user)
        }
        await self.broadcast(json)

    async def handle_message(self, user: str, message: dict[str, str]):
        """Handler message from user."""

        ######### [ TODO ] #########
        # TODO Check the message type and receiver.
        ############################
        msg_type = message["type"]
        msg = message["msg"]
        if msg_type == "direct":
            dst_user = message["to"]
            try:
                dst_socket = self.members[dst_user]
                await dst_socket.send_json(
                    {
                        "from": dst_user,
                        "msg": msg
                    }
                )
            except KeyError:
                src_socket = self.members[user]
                await src_socket.send_json(
                    {
                        "from": "system",
                        "msg": "User {} does not exist.".format(dst_user)
                    }
                )

        else:
            await self.broadcast(
                {
                    "from":user,
                    "msg":msg
                }, 1, user
            )

        ######### [ TODO ] #########
        # TODO If the valid receiver does not exist, send error message back to the sender.
        ############################

        ######### [ TODO ] #########
        # TODO Otherwise, forward the message to the receiver.
        # If broadcasting the message, DO NOT send to the original sender.
        ############################

    async def broadcast(self, msg: dict, type = 0, sender = None):
        tasks = []
        for user, socket in self.members.items():
            if type == 1 and sender == user:
                continue
            task = asyncio.create_task(socket.send_json(msg))
            tasks.append(task)

        for task in tasks:
            await task
