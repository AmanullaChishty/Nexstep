# inbox/gmail.py
# For dev: start with pull (list last N messages). Add push/webhook later.
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

def list_recent_messages(creds_json: dict, query="newer_than:30d", max_results=50):
    creds = Credentials.from_authorized_user_info(creds_json, scopes=[
        "https://www.googleapis.com/auth/gmail.readonly"
    ])
    service = build("gmail", "v1", credentials=creds)
    res = service.users().messages().list(userId="me", q=query, maxResults=max_results).execute()
    ids = [m["id"] for m in res.get("messages", [])]
    msgs = []
    for mid in ids:
        msg = service.users().messages().get(userId="me", id=mid, format="full").execute()
        msgs.append(msg)
    return msgs
