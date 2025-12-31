from telethon import TelegramClient, events
from telethon.sessions import StringSession
import time
import sys

# ===== DETAILS =====
api_id = 32557753              # apna API ID
api_hash = "3aec7775e6af24432f2414f941409876"     # apna API HASH
STRING_SESSION = "1BVtsOG0Bu6MwOfO9kH6eIuGTByS9Umtj0N68MX5_vfXxwe2FwpWaMdHZkb2ptbAAv9Klo-XjQoEzeQYf2Iq2cpXq6TZax9AkeTjr4bOoK_9QLVCUSIPXWlvGnP65x5fWRoq-fzSuPJaqJkhS1K3Zn4U9wOxgu2viwVsXoHICuc8TlHpZS4WTnQjATVX-_dnn97dtoBmDbln9tAch_Jea_I3ltQv3_XzRBTVhjO88zc4LPhaCsjf11CF8zpKuJGced81bj5H3zrPB0TXJaMOHIgXKD8yWc-qmy9qNMKZZENsf7zi0gPsBVEZKKa59y9pciD_c39gkgu9dzKHXlB49vZYhkcvgjsE="
# ===================

if not STRING_SESSION or len(STRING_SESSION) < 50:
    print("❌ Invalid STRING_SESSION")
    sys.exit(1)

client = TelegramClient(StringSession(STRING_SESSION), api_id, api_hash)

IDLE_LIMIT = 1  # seconds
last_active_time = time.time()
last_offline_state = False
replied_users = set()

# -----------------------------
# Track your activity (ONLINE)
# -----------------------------
@client.on(events.NewMessage(from_users='me'))
async def track_activity(event):
    global last_active_time, replied_users, last_offline_state
    last_active_time = time.time()
    replied_users.clear()
    last_offline_state = False

# -----------------------------
# Auto reply in DM when OFFLINE
# -----------------------------
@client.on(events.NewMessage(incoming=True))
async def auto_reply_dm(event):
    global last_offline_state, replied_users

    if not event.is_private or event.out:
        return

    idle_time = time.time() - last_active_time
    offline_now = idle_time >= IDLE_LIMIT

    # new offline cycle
    if offline_now and not last_offline_state:
        replied_users.clear()
        last_offline_state = True

    if not offline_now:
        return

    if event.sender_id in replied_users:
        return

    replied_users.add(event.sender_id)

    await event.reply(
        "ʜɪ\n\n"
        "I Aᴍ Oꜰꜰʟɪɴᴇ Aɴᴅ Cᴏᴍᴇ Oɴʟɪɴᴇ Sᴏᴏɴ "
        "Aɴᴅ Rᴇᴩʟy Yᴏᴜ 😴😴"
    )

print("🚀 Userbot started")
client.start()
client.run_until_disconnected()
