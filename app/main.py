from fastapi import FastAPI
from .db import init_db
from .auth.router import router as auth_router
from .inbox.router import router as inbox_router
from .tasks.router import router as tasks_router
from .calendar.router import router as cal_router
from .reports.router import router as reports_router

app = FastAPI(title="OpsCo Pilot")

@app.on_event("startup")
def on_startup():
    init_db()

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(inbox_router, prefix="/inbox", tags=["inbox"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
app.include_router(cal_router, prefix="/calendar", tags=["calendar"])
app.include_router(reports_router, prefix="/reports", tags=["reports"])
