# calendar/booking.py
from datetime import datetime, timedelta
from typing import List, Tuple

def merge_busy(busy_blocks: List[Tuple[datetime, datetime]], buffer_min=15):
    busy_blocks = sorted(busy_blocks, key=lambda x: x[0])
    merged = []
    for s,e in busy_blocks:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)
    # add buffer
    buf = []
    for s,e in merged:
        buf.append((s - timedelta(minutes=buffer_min), e + timedelta(minutes=buffer_min)))
    return buf

def find_slots(busy: List[Tuple[datetime, datetime]], day_start: datetime, day_end: datetime, duration_min=30, notice_min=720):
    slots = []
    now = datetime.utcnow() + timedelta(minutes=notice_min)
    b = merge_busy(busy)
    cur = max(day_start, now)
    for s,e in b:
        if cur + timedelta(minutes=duration_min) <= s:
            slots.append((cur, min(s, day_end)))
        cur = max(cur, e)
        if cur >= day_end: break
    if cur + timedelta(minutes=duration_min) <= day_end:
        slots.append((cur, day_end))
    # return slot starts (cap to next few)
    starts = []
    for s,e in slots:
        t = s
        while t + timedelta(minutes=duration_min) <= e:
            starts.append(t)
            t += timedelta(minutes=duration_min)
    return starts[:10]
