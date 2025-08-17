# reports/weekly.py
from datetime import datetime, timedelta
from sqlmodel import Session, select
from ..models import Task, Message

def build_weekly_summary(session: Session, user_id: int) -> str:
    since = datetime.utcnow() - timedelta(days=7)
    leads = session.exec(select(Task).where(Task.user_id==user_id, Task.title.ilike("%lead%"), Task.created_at>=since)).all()
    invoices = session.exec(select(Task).where(Task.user_id==user_id, Task.title.ilike("%invoice%"), Task.created_at>=since)).all()
    # TODO: stalled threads, meetings
    lines = [
        f"Weekly Summary",
        f"- New leads: {len(leads)}",
        f"- Invoice mentions: {len(invoices)}",
        "- Stalled threads: TODO",
        "- Meetings scheduled: TODO",
    ]
    return "\n".join(lines)
