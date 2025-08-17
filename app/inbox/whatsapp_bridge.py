# inbox/whatsapp_bridge.py
from email.parser import BytesParser
from email.policy import default

def parse_whatsapp_email(raw_bytes: bytes):
    msg = BytesParser(policy=default).parsebytes(raw_bytes)
    subject = msg["subject"] or ""
    from_addr = msg["from"]
    to_addr = msg["to"]
    body = msg.get_body(preferencelist=("plain",)).get_content()
    return {
        "source": "whatsapp",
        "subject": subject,
        "from": from_addr,
        "to": to_addr,
        "text": body
    }
