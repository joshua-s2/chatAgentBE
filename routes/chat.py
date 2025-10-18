from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from services import chat_service
from database import SessionLocal
from pydantic import BaseModel

router = APIRouter()

class ChatRequest(BaseModel):
    session_id: str
    message: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/chats")
def create_chat(chat: ChatRequest, db: Session = Depends(get_db)):
    """
    POST /api/chats
    Accepts JSON body: { session_id, message }
    """
    return chat_service.create_chat(chat.session_id, chat.message)

@router.get("/chats/{session_id}")
def get_chats(session_id: str, db: Session = Depends(get_db)):
    """
    GET /api/chats/{session_id}
    Retrieve all messages for a session
    """
    chats = chat_service.get_chats(session_id)
    return chats if chats else []
