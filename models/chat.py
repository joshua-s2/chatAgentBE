from pydantic import BaseModel
from typing import Optional

class Chat(BaseModel):
    id: Optional[int] = None
    session_id: str
    message: str
    response: Optional[str] = None
