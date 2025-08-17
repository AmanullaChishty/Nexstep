# inbox/outlook.py
# Use MS Graph; for dev, pull last N emails.
import requests
def list_recent_messages(access_token: str, top=50):
    headers = {"Authorization": f"Bearer {access_token}"}
    url = "https://graph.microsoft.com/v1.0/me/messages?$top={}&$orderby=receivedDateTime desc".format(top)
    r = requests.get(url, headers=headers, timeout=20)
    r.raise_for_status()
    return r.json().get("value", [])
