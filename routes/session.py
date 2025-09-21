from fastapi import APIRouter
from pydantic import BaseModel
from services import session_service

router = APIRouter()

class SessionCreate(BaseModel):
    name: str

@router.post("/sessions")
def create_session(session: SessionCreate):
    return session_service.create_session(session.name)

@router.get("/sessions")
def get_sessions():
    return session_service.get_sessions()
