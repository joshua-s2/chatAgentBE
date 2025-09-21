
from pydantic import BaseModel
from typing import Optional

class Session(BaseModel):
    id: Optional[str] = None
    name: str
