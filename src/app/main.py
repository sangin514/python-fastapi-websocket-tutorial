from fastapi import FastAPI

from src.app.chat.router import router as chat_router


app = FastAPI()
app.include_router(chat_router)


@app.get("/")
def root():
    return {"messgae": "Hello, world!"}