# ==========================================
# 🚀 ONE FILE INTELLIGENT SCHEDULER (SMART AI VERSION)
# ==========================================

from datetime import datetime, timedelta
from collections import Counter
import re

# ==============================
# 🔑 CONFIG
# ==============================

BUFFER_MINUTES = 15
WORK_START = 9
WORK_END = 18

# ==============================
# 📅 MOCK CALENDAR DATA
# ==============================

def get_events():
    return [
        {"title":"Standup","start":datetime(2026,2,10,10,0),"end":datetime(2026,2,10,10,30),"recurring":True,"cancelled":False},
        {"title":"Client Call","start":datetime(2026,2,10,14,0),"end":datetime(2026,2,10,15,0),"recurring":False,"cancelled":True},
        {"title":"Team Sync","start":datetime(2026,2,10,16,0),"end":datetime(2026,2,10,16,30),"recurring":True,"cancelled":False},
    ]

# ==============================
# 📉 SCALEDOWN TEMP FIX
# ==============================

def compress_history(events):

    print("\n📉 ScaleDown Compression Applied (Simulated)")

    original = len(events)
    compressed = max(1, int(original * 0.2))

    print(f"Original events: {original}")
    print(f"Compressed size: {compressed}")
    print("✅ 80% memory reduction achieved")

# ==============================
# 📊 ANALYTICS
# ==============================

def analytics(events):

    total = len(events)
    cancelled = sum(1 for e in events if e["cancelled"])
    recurring = sum(1 for e in events if e["recurring"])

    print("\n📊 Meeting Analytics")
    print("Total:", total)
    print("Cancelled:", cancelled)
    print("Recurring:", recurring)

# ==============================
# 🧠 SMART COMMAND PARSER (NEW)
# ==============================

def parse_command(cmd):

    settings = {
        "preferred_hour": None,
        "avoid_morning": False,
        "priority": "normal"
    }

    # detect hour like "3pm" or "11"
    match = re.search(r'(\d{1,2})\s*(am|pm)?', cmd)

    if match:
        hour = int(match.group(1))
        ampm = match.group(2)

        if ampm == "pm" and hour < 12:
            hour += 12

        settings["preferred_hour"] = hour

    if "avoid morning" in cmd or "avoid mornings" in cmd:
        settings["avoid_morning"] = True

    if "high priority" in cmd:
        settings["priority"] = "high"

    print("\n🧠 Parsed Command Settings:", settings)

    return settings

# ==============================
# 🧠 PREFERENCE LEARNER
# ==============================

def learn_preferences(events, cmd_settings):

    if cmd_settings["preferred_hour"] is not None:
        pref = cmd_settings["preferred_hour"]
    else:
        hours = [e["start"].hour for e in events]
        pref = Counter(hours).most_common(1)[0][0]

    print("\n🧠 Preferred Hour:", pref)

    return {"preferred_hour":pref}

# ==============================
# ⚠️ CANCELLATION PREDICTOR
# ==============================

def predict_cancellation(events):

    risky = set(e["start"].hour for e in events if e["cancelled"])

    print("⚠️ Risky Hours:", risky)

    return risky

# ==============================
# 🟢 AVAILABILITY AGENT
# ==============================

def find_free_slots(events, cmd_settings):

    free = []

    current = datetime(2026,2,10,WORK_START,0)

    for e in sorted(events, key=lambda x: x["start"]):

        start_with_buffer = e["start"] - timedelta(minutes=BUFFER_MINUTES)

        if current < start_with_buffer:
            free.append(current)

        current = e["end"] + timedelta(minutes=BUFFER_MINUTES)

    end_day = datetime(2026,2,10,WORK_END,0)

    if current < end_day:
        free.append(current)

    # apply avoid morning rule
    if cmd_settings["avoid_morning"]:
        free = [s for s in free if s.hour >= 12]

    print("\n🟢 Free Slots:", free)

    return free

# ==============================
# 🤝 NEGOTIATION
# ==============================

def negotiate_slots(list_of_slots):

    common = set(list_of_slots[0])

    for s in list_of_slots[1:]:
        common = common.intersection(set(s))

    result = list(common)

    print("\n🤝 Negotiated Slots:", result)

    return result

# ==============================
# ⚙️ OPTIMIZER AGENT
# ==============================

def score_slot(slot, preferences, risky_hours, cmd_settings):

    score = 0

    if slot.hour == preferences["preferred_hour"]:
        score += 10

    if slot.hour in risky_hours:
        score -= 5

    if 9 <= slot.hour <= 12:
        score += 3

    if cmd_settings["priority"] == "high":
        score += 5

    return score


def choose_best_slot(slots, preferences, risky_hours, cmd_settings):

    best = None
    best_score = -999

    for s in slots:
        sc = score_slot(s, preferences, risky_hours, cmd_settings)
        print(f"Slot {s} score = {sc}")

        if sc > best_score:
            best_score = sc
            best = s

    print("\n⭐ BEST SLOT:", best)

    return best

# ==============================
# 📅 CREATE EVENT
# ==============================

def create_event(slot):

    print(f"\n📅 Meeting Scheduled Successfully at {slot}")

# ==============================
# 🚀 MAIN SCHEDULER
# ==============================

def run_scheduler(cmd_settings):

    print("\n🚀 SMART AI SCHEDULER STARTED\n")

    events = get_events()

    compress_history(events)

    analytics(events)

    prefs = learn_preferences(events, cmd_settings)

    risky = predict_cancellation(events)

    free_slots = find_free_slots(events, cmd_settings)

    participant2 = free_slots[:]

    common_slots = negotiate_slots([free_slots, participant2])

    best = choose_best_slot(common_slots, prefs, risky, cmd_settings)

    if best:
        create_event(best)

    print("\n✅ Scheduling Complete!")

# ==============================
# 🤖 COMMAND INTERFACE
# ==============================

def command_interface():

    print("💬 Enter smart command:")
    cmd = input(">>> ").lower()

    if "schedule" in cmd:
        settings = parse_command(cmd)
        run_scheduler(settings)
    else:
        print("❌ Unknown command. Try: schedule meeting tomorrow at 3pm")

# ==============================

if __name__ == "__main__":
    command_interface()
