from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from services import session_service
from database import SessionLocal

router = APIRouter()

class SessionCreate(BaseModel):
    name: str


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/sessions")
def create_session(session: SessionCreate, db: Session = Depends(get_db)):
    return session_service.create_session(session.name)

@router.get("/sessions")
def get_sessions(db: Session = Depends(get_db)):
    return session_service.get_sessions()
