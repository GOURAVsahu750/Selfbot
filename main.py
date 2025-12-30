from telethon import TelegramClient, events
import time
import os

# ===== APNI DETAILS =====
api_id = 32557753              # <-- apna API ID
api_hash = "3aec7775e6af24432f2414f941409876"     # <-- apna API HASH
session_name = "titan_userbot"
# ========================

client = TelegramClient(session_name, api_id, api_hash)

IDLE_LIMIT = 5  # seconds (5 sec idle = offline)
last_active_time = time.time()
replied_users = set()

# -----------------------------
# Track your own activity
# -----------------------------
@client.on(events.NewMessage(from_users='me'))
async def track_activity(event):
    global last_active_time, replied_users
    last_active_time = time.time()
    replied_users.clear()

# -----------------------------
# Auto reply ONLY in DM
# -----------------------------
@client.on(events.NewMessage(incoming=True))
async def auto_reply_dm(event):
    if not event.is_private:
        return

    if event.out:
        return

    idle_time = time.time() - last_active_time

    # Agar online ho (5 sec se kam idle)
    if idle_time < IDLE_LIMIT:
        return

    # Same user ko baar-baar reply na ho
    if event.sender_id in replied_users:
        return

    replied_users.add(event.sender_id)

    await event.reply(
        "ʜɪ\n\n"
        "I Aᴍ Oꜰꜰʟɪɴᴇ Aɴᴅ Cᴏᴍᴇ Oɴʟɪɴᴇ Sᴏᴏɴ "
        "Aɴᴅ Rᴇᴩʟy Yᴏᴜ 😴😴"
    )

print("🚀 Telegram Userbot started on Railway")
client.start()
client.run_until_disconnected()