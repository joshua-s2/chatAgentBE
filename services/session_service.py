from sqlalchemy.orm import Session
from models.session import Session as SessionModel
from database import SessionLocal
import uuid

def create_session(name: str):
    db = SessionLocal()
    session = SessionModel(id=str(uuid.uuid4()), name=name)
    db.add(session)
    db.commit()
    db.refresh(session)
    db.close()
    return session

def get_sessions():
    db = SessionLocal()
    sessions = db.query(SessionModel).all()
    db.close()
    return sessions
