import time
import asyncio
from telethon import TelegramClient, events
from telethon.sessions import StringSession

api_id = 32557753
api_hash = "3aec7775e6af24432f2414f941409876"
STRING_SESSION = "1BVtsOG0Bu6MwOfO9kH6eIuGTByS9Umtj0N68MX5_vfXxwe2FwpWaMdHZkb2ptbAAv9Klo-XjQoEzeQYf2Iq2cpXq6TZax9AkeTjr4bOoK_9QLVCUSIPXWlvGnP65x5fWRoq-fzSuPJaqJkhS1K3Zn4U9wOxgu2viwVsXoHICuc8TlHpZS4WTnQjATVX-_dnn97dtoBmDbln9tAch_Jea_I3ltQv3_XzRBTVhjO88zc4LPhaCsjf11CF8zpKuJGced81bj5H3zrPB0TXJaMOHIgXKD8yWc-qmy9qNMKZZENsf7zi0gPsBVEZKKa59y9pciD_c39gkgu9dzKHXlB49vZYhkcvgjsE="

OFFLINE_AFTER = 1  # seconds
REPLY_DELAY = 1   # seconds

last_active = time.time()

client = TelegramClient(
    StringSession(STRING_SESSION),
    api_id,
    api_hash
)

@client.on(events.NewMessage(from_users='me'))
async def mark_online(event):
    global last_active
    last_active = time.time()

@client.on(events.NewMessage(incoming=True))
async def auto_reply(event):
    if not event.is_private or event.out:
        return

    if time.time() - last_active < OFFLINE_AFTER:
        return

    await asyncio.sleep(REPLY_DELAY)

    await client.send_message(
        event.chat_id,
        "ʜɪ\n\n"
        "I Aᴍ Oꜰꜰʟɪɴᴇ Aɴᴅ Cᴏᴍᴇ Oɴʟɪɴᴇ Sᴏᴏɴ "
        "Aɴᴅ Rᴇᴩʟy Yᴏᴜ 😴😴"
    )

async def main():
    await client.start()
    print("✅ Userbot running on Koyeb")
    await asyncio.Event().wait()

asyncio.run(main())
