# auth/router.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel, EmailStr
from sqlmodel import Session, select
from ..db import get_session
from ..models import User
from ..config import settings
from ..utils.email_send import send_email
from .magic_link import generate_token, verify_token

router = APIRouter()

class MagicLinkRequest(BaseModel):
    email: EmailStr

@router.post("/magic-link")
def request_magic_link(payload: MagicLinkRequest, session: Session = Depends(get_session)):
    token = generate_token(payload.email)
    link = f"{settings.FRONTEND_URL}/login/callback?token={token}"
    send_email(to=payload.email, subject="Your login link", text=f"Sign in: {link}")
    return {"ok": True}

class TokenIn(BaseModel):
    token: str

@router.post("/callback")
def login_callback(payload: TokenIn, session: Session = Depends(get_session)):
    email = verify_token(payload.token)
    if not email:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = session.exec(select(User).where(User.email == email)).first()
    if not user:
        user = User(email=email)
        session.add(user); session.commit(); session.refresh(user)
    # Return a simple session token (JWT could be added)
    return {"ok": True, "user": {"id": user.id, "email": user.email}}
