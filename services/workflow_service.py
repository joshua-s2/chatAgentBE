from typing import List
from models.workflow import Workflow

workflows: List[Workflow] = []
workflow_counter = 1

def create_workflow(name: str, policy: str, escalation: bool) -> Workflow:
    global workflow_counter
    wf = Workflow(id=workflow_counter, name=name, policy=policy, escalation=escalation)
    workflows.append(wf)
    workflow_counter += 1
    return wf

def get_workflows() -> List[Workflow]:
    return workflows

def get_workflow_policy() -> str:
    """Return concatenated policy text from all workflows (or the relevant one)."""
    if not workflows:
        return "No workflow defined."
    return workflows[-1].policy
