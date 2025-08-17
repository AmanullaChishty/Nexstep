# auth/magic_link.py
import hmac, hashlib, base64, time
from ..config import settings

def generate_token(email: str, ttl_sec: int = 900) -> str:
    exp = int(time.time()) + ttl_sec
    msg = f"{email}|{exp}".encode()
    sig = hmac.new(settings.SECRET_KEY.encode(), msg, hashlib.sha256).digest()
    b = base64.urlsafe_b64encode(msg + b"|" + sig).decode()
    return b

def verify_token(token: str) -> str | None:
    try:
        data = base64.urlsafe_b64decode(token.encode())
        parts = data.split(b"|")
        email, exp, sig = parts[0].decode(), int(parts[1].decode()), parts[2]
        if int(time.time()) > exp: return None
        msg = f"{email}|{exp}".encode()
        exp_sig = hmac.new(settings.SECRET_KEY.encode(), msg, hashlib.sha256).digest()
        if hmac.compare_digest(sig, exp_sig):
            return email
    except Exception:
        return None
    return None
