import asyncio
from fastapi import WebSocket


class Chat:
    members: dict[str, WebSocket]

    """Represents the chatting room."""
    def __init__(self):
        self.members = {}
    
    async def join(self, user: str, websocket: WebSocket):
        """Connect to the user and add user to the members on success."""

        ######### [ TODO ] #########
        # TODO Establish connection
        ############################

        ######### [ TODO ] #########
        # TODO Close connection on duplicate and exit method.
        ############################

        ######### [ TODO ] #########
        # TODO Otherwise, add user to the members.
        ############################

        ######### [ TODO ] #########
        # TODO Optionally, broadcast the system message that the user joined the chat.
        ############################

    async def leave(self, user: str):
        """Remove user from the members."""

        ######### [ TODO ] #########
        # TODO Remove user from the members.
        ############################
    
        ######### [ TODO ] #########
        # TODO Optionally, broadcast the system message that the user left the chat.
        ############################

    async def handle_message(self, user: str, message: dict[str, str]):
        """Handler message from user."""

        ######### [ TODO ] #########
        # TODO Check the message type and receiver.
        ############################

        ######### [ TODO ] #########
        # TODO If the valid receiver does not exist, send error message back to the sender.
        ############################

        ######### [ TODO ] #########
        # TODO Otherwise, forward the message to the receiver.
        # If broadcasting the message, DO NOT send to the original sender.
        ############################
