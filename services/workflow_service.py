from sqlalchemy.orm import Session
from models.workflow import Workflow
from database import SessionLocal
from fastapi import HTTPException

def create_workflow(name: str, policy: str, escalation: bool):
    if not name.strip():
        raise HTTPException(status_code=400, detail="Workflow name cannot be empty.")
    if not policy.strip():
        raise HTTPException(status_code=400, detail="Workflow policy cannot be empty.")
    db = SessionLocal()
    try:
        existing = db.query(Workflow).filter(Workflow.name == name).first()
        if existing:
            existing.policy = policy
            existing.escalation = escalation
            db.commit()
            db.refresh(existing)
            return {"status": "updated", "workflow": existing}
        
        workflow = Workflow(name=name, policy=policy, escalation=escalation)
        db.add(workflow)
        db.commit()
        db.refresh(workflow)
        return {"status": "created", "workflow": workflow}
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()

def get_workflows():
    db = SessionLocal()
    try:
        return db.query(Workflow).all()
    finally:
        db.close()

def get_workflow_policy() -> str:
    db = SessionLocal()
    try:
        wf = db.query(Workflow).order_by(Workflow.id.desc()).first()
        if not wf:
            return "No workflow defined."
        return wf.policy
    finally:
        db.close()
