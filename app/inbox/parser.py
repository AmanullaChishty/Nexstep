# inbox/parser.py
import re
from datetime import datetime

CURRENCY = r"(?:USD|EUR|INR|\$|€|₹)"
DATE_PAT = r"\b(?:\d{4}-\d{2}-\d{2}|\d{1,2}/\d{1,2}/\d{2,4})\b"

def normalize_email_message(gmail_like: dict) -> dict:
    headers = gmail_like.get("payload", {}).get("headers", [])
    h = {x["name"].lower(): x["value"] for x in headers}
    subject = h.get("subject", "")
    sender = h.get("from", "")
    to = h.get("to", "")
    ts = int(gmail_like.get("internalDate", 0)) // 1000
    # Get plain text
    body_text = ""
    parts = gmail_like.get("payload", {}).get("parts", [])
    if parts:
        for p in parts:
            if p.get("mimeType") == "text/plain":
                import base64
                body_text = base64.urlsafe_b64decode(p["body"]["data"]).decode(errors="ignore")
                break
    return {
        "subject": subject,
        "sender": sender,
        "to": to,
        "body_text": body_text,
        "ts": datetime.utcfromtimestamp(ts),
    }

def extract_entities(text: str) -> dict:
    ents = {}
    if m:= re.search(CURRENCY + r"\s?\d[\d,]*(?:\.\d+)?", text, re.I):
        ents["amount"] = m.group(0)
    if m:= re.search(r"\b(?:invoice|payment|paid|unpaid|due)\b", text, re.I):
        ents["billing"] = True
    if m:= re.search(r"\b(?:proposal|quote|estimate|SOW)\b", text, re.I):
        ents["proposal"] = True
    if m:= re.search(r"\b(?:call|meet|schedule|reschedul|time)\b", text, re.I):
        ents["meeting"] = True
    if m:= re.search(DATE_PAT, text):
        ents["date"] = m.group(0)
    return ents
