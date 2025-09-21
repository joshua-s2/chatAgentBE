from fastapi import APIRouter
from pydantic import BaseModel
from services import workflow_service

router = APIRouter()

class WorkflowCreate(BaseModel):
    name: str
    policy: str
    escalation: bool

@router.post("/workflow")
def create_workflow(workflow: WorkflowCreate):
    return workflow_service.create_workflow(
        workflow.name, workflow.policy, workflow.escalation
    )

@router.get("/workflow")
def get_workflows():
    return workflow_service.get_workflows()
