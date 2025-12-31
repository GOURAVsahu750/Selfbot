import time
import sys
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

# ===== DETAILS =====
api_id = 32557753              # apna API ID
api_hash = "3aec7775e6af24432f2414f941409876"     # apna API HASH
STRING_SESSION = "1BVtsOG0Bu6MwOfO9kH6eIuGTByS9Umtj0N68MX5_vfXxwe2FwpWaMdHZkb2ptbAAv9Klo-XjQoEzeQYf2Iq2cpXq6TZax9AkeTjr4bOoK_9QLVCUSIPXWlvGnP65x5fWRoq-fzSuPJaqJkhS1K3Zn4U9wOxgu2viwVsXoHICuc8TlHpZS4WTnQjATVX-_dnn97dtoBmDbln9tAch_Jea_I3ltQv3_XzRBTVhjO88zc4LPhaCsjf11CF8zpKuJGced81bj5H3zrPB0TXJaMOHIgXKD8yWc-qmy9qNMKZZENsf7zi0gPsBVEZKKa59y9pciD_c39gkgu9dzKHXlB49vZYhkcvgjsE="
# ===================

# ---------- SAFETY CHECK ----------
if not STRING_SESSION or len(STRING_SESSION) < 50:
    print("❌ Invalid STRING_SESSION")
    sys.exit(1)

# ---------- CLIENT ----------
client = TelegramClient(
    StringSession(STRING_SESSION),
    api_id,
    api_hash,
    connection_retries=10,
    timeout=30
)

# ---------- SETTINGS ----------
IDLE_LIMIT = 1  # 1 second offline trigger
last_active_time = time.time()

# ---------- ONLINE TRACK ----------
@client.on(events.NewMessage(from_users='me'))
async def track_activity(event):
    global last_active_time
    last_active_time = time.time()

# ---------- OFFLINE AUTO REPLY ----------
@client.on(events.NewMessage(incoming=True))
async def auto_reply_dm(event):

    if not event.is_private or event.out:
        return

    offline_now = (time.time() - last_active_time) >= IDLE_LIMIT
    if not offline_now:
        return

    # 1 second delay
    await asyncio.sleep(1)

    await client.send_message(
        event.chat_id,
        "ʜɪ\n\n"
        "I Aᴍ Oꜰꜰʟɪɴᴇ Aɴᴅ Cᴏᴍᴇ Oɴʟɪɴᴇ Sᴏᴏɴ "
        "Aɴᴅ Rᴇᴩʟy Yᴏᴜ 😴😴"
    )

# ---------- MAIN ----------
async def main():
    print("⏳ Connecting to Telegram...")
    await client.start()
    print("✅ Connected")
    await client.run_until_disconnected()

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print("❌ Fatal error:", e)
