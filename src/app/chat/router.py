from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

from src.app.chat.chat import Chat


chat = Chat()
router = APIRouter(prefix="/chat", tags=['chat'])
with open('assets/index.html', 'r') as f:
    html = f.read()


@router.get("/")
async def get() -> HTMLResponse:
    """Loads the web page."""
    return HTMLResponse(html)


@router.websocket("/ws")
async def websocket(user: str, websocket: WebSocket):
    """Interact with user via connection."""

    ######### [ TODO ] #########
    # TODO Join the chat
    ############################

    try:
        while True:
            ######### [ TODO ] #########
            # TODO Receive message from the user and handle
            ############################
            pass
    except WebSocketDisconnect:
        ######### [ TODO ] #########
        # TODO Handle disconnection: leave the chat
        ############################
        pass
