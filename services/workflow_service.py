from sqlalchemy.orm import Session
from models.workflow import Workflow
from database import SessionLocal

def create_workflow(name: str, policy: str, escalation: bool):
    db = SessionLocal()
    workflow = Workflow(name=name, policy=policy, escalation=escalation)
    db.add(workflow)
    db.commit()
    db.refresh(workflow)
    db.close()
    return workflow

def get_workflows():
    db = SessionLocal()
    workflows = db.query(Workflow).all()
    db.close()
    return workflows

def get_workflow_policy() -> str:
    db = SessionLocal()
    wf = db.query(Workflow).order_by(Workflow.id.desc()).first()
    db.close()
    if not wf:
        return "No workflow defined."
    return wf.policy
