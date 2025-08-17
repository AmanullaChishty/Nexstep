# tasks/service.py
from datetime import datetime, timedelta
from sqlmodel import Session
from ..models import Task, Intent, Thread

INTENT_DEFAULT_TITLES = {
    "lead": "New lead: review and reply",
    "proposal": "Proposal: prepare or confirm",
    "invoice": "Invoice/payment: follow up",
    "meeting": "Meeting: schedule/confirm",
    "review": "Review message"
}

def create_task_for_intent(session: Session, user_id: int, thread_id: int, intent: Intent):
    title = INTENT_DEFAULT_TITLES.get(intent.type, "Action needed")
    due_at = datetime.utcnow() + timedelta(days=2)
    task = Task(user_id=user_id, thread_id=thread_id, intent_id=intent.id, title=title, status="new", due_at=due_at)
    session.add(task); session.commit(); session.refresh(task)
    return task
