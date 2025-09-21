from typing import List
from models.session import Session

sessions: List[Session] = []
session_counter = 1

def create_session(name: str) -> Session:
    global session_counter
    session = Session(id=session_counter, name=name)
    sessions.append(session)
    session_counter += 1
    return session

def get_sessions() -> List[Session]:
    return sessions
