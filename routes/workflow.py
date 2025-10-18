from fastapi import APIRouter, HTTPException, Request
from services import workflow_service

router = APIRouter(prefix="/api/workflow", tags=["Workflow"])


@router.post("")
async def create_workflow(request: Request):
    data = await request.json()
    name = data.get("name", "").strip()
    policy = data.get("policy", "").strip()
    escalation = bool(data.get("escalation", False))
    try:
        result = workflow_service.create_workflow(name, policy, escalation)
        return {
            "status": result["status"],
            "workflow": {
                "id": result["workflow"].id,
                "name": result["workflow"].name,
                "policy": result["workflow"].policy,
                "escalation": result["workflow"].escalation,
            },
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@router.get("")
async def get_workflows():
    try:
        workflows = workflow_service.get_workflows()
        return [
            {
                "id": wf.id,
                "name": wf.name,
                "policy": wf.policy,
                "escalation": wf.escalation,
            }
            for wf in workflows
        ]
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")


@router.get("/policy")
async def get_workflow_policy():
    try:
        policy = workflow_service.get_workflow_policy()
        return {"policy": policy}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {str(e)}")
