# inbox/intents.py
import re
from .parser import extract_entities

def classify(text: str) -> tuple[str, float, dict]:
    t = text.lower()
    ents = extract_entities(text)
    # meeting
    if re.search(r"\b(schedule|reschedul|meet|call|availability|slots)\b", t):
        return ("meeting", 0.9, ents)
    # invoice/payment
    if re.search(r"\b(invoice|payment|paid|unpaid|overdue|remit|bank transfer)\b", t):
        return ("invoice", 0.9, ents)
    # proposal/quote
    if re.search(r"\b(proposal|quote|estimate|send over|pricing|rate card)\b", t):
        return ("proposal", 0.85, ents)
    # new lead (generic inquiry)
    if re.search(r"\b(interested|project|build|need help|looking for)\b", t):
        return ("lead", 0.8, ents)
    # fallback
    return ("review", 0.5, ents)
