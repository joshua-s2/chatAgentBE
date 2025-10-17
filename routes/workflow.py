from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel
from services import workflow_service
from database import SessionLocal

router = APIRouter()

class WorkflowCreate(BaseModel):
    name: str
    policy: str
    escalation: bool

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/workflow")
def create_workflow(workflow: WorkflowCreate, db: Session = Depends(get_db)):
    return workflow_service.create_workflow(
        workflow.name, workflow.policy, workflow.escalation
    )

@router.get("/workflow")
def get_workflows(db: Session = Depends(get_db)):
    return workflow_service.get_workflows()
