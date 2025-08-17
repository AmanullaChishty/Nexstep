# models.py
from typing import Optional, List
from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    email: str = Field(index=True, unique=True)
    name: str | None = None
    tz: str = "UTC"
    plan: str = "pro"
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Connection(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id")
    type: str  # gmail,outlook,gcal,mscal,whatsapp_bridge
    access_token: str | None = None
    refresh_token: str | None = None
    metadata: str | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Thread(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    source: str  # email_gmail, email_outlook, whatsapp
    subject: str | None = None
    participants: str | None = None  # JSON string
    last_message_at: datetime | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Message(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    thread_id: int = Field(foreign_key="thread.id", index=True)
    source: str
    sender: str
    to: str | None = None
    cc: str | None = None
    body_text: str | None = None
    body_html: str | None = None
    ts: datetime = Field(default_factory=datetime.utcnow)

class Intent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    thread_id: int = Field(foreign_key="thread.id", index=True)
    type: str  # lead, proposal, meeting, invoice, scope, support, status
    confidence: float = 0.0
    entities: str | None = None  # JSON
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Task(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    thread_id: int | None = Field(default=None, foreign_key="thread.id")
    intent_id: int | None = Field(default=None, foreign_key="intent.id")
    title: str
    status: str = "new"  # new, waiting, action, scheduled, done
    due_at: datetime | None = None
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Meeting(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_id: int = Field(foreign_key="user.id", index=True)
    thread_id: int | None = Field(default=None, foreign_key="thread.id")
    start_at: datetime | None = None
    end_at: datetime | None = None
    attendees: str | None = None  # JSON emails
    status: str = "tentative"
    created_at: datetime = Field(default_factory=datetime.utcnow)
