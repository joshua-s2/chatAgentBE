from fastapi import APIRouter, Body
from services import chat_service
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str

@router.post("/chats")
def create_chat(chat: ChatRequest):
    """
    POST /api/chats
    Accepts JSON body: { session_id, message }
    """
    return chat_service.create_chat(chat.session_id, chat.message)

@router.get("/chats/{session_id}")
def get_chats(session_id: str):
    """
    GET /api/chats/{session_id}
    Retrieve all messages for a session
    """
    return chat_service.get_chats(session_id)
