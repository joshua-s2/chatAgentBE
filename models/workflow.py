from pydantic import BaseModel
from typing import Optional

class Workflow(BaseModel):
    id: Optional[int] = None
    name: str
    policy: str
    escalation: bool
