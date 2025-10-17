from pydantic import BaseModel
from typing import Optional

class WorkflowCreate(BaseModel):
    name: str
    policy: str
    escalation: bool

class WorkflowResponse(WorkflowCreate):
    id: int
    class Config:
        orm_mode = True
