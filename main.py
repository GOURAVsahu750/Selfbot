from telethon import TelegramClient, events
from telethon.sessions import StringSession
import time

api_id = 32557753
api_hash = "3aec7775e6af24432f2414f941409876"
STRING_SESSION = "1BVtsOKYBuzSXbkJ15Yjx9HhYTF8Frf5K1W3jFVFA1kW064TjA_Twb8VkAczmuzVLTh_Y0We9Mvf0lWsalFPjxdrPs6KtLN9EvJwcbW81w9svCSazjRnDhWxPYZ44-rrhXl1Lh8mAGL8L4NwM-tmm_Gyrfuk7blSPtOYJYCXKg6uKmPKKwkEhwvTgGj-eQIqgFYgHLZZ4zM8t_18qRtMcx2uL5K06hebzd-zVoeYhdqsTbDbIiVi_2cLJehskL1tHU73oSsqH4gN3ExF5rvgvcT3wBtO9u1xD7kDwpOVAUwvwPwvk2XjnISTqvK_zcDZL0gfNVHdjuk71ksUVmhGossJiY4Rx4yw="

client = TelegramClient(StringSession(STRING_SESSION), api_id, api_hash)

IDLE_LIMIT = 5
last_active_time = time.time()
replied_users = set()

@client.on(events.NewMessage(from_users='me'))
async def track_activity(event):
    global last_active_time, replied_users
    last_active_time = time.time()
    replied_users.clear()

@client.on(events.NewMessage(incoming=True))
async def auto_reply_dm(event):
    if not event.is_private or event.out:
        return

    if time.time() - last_active_time < IDLE_LIMIT:
        return

    if event.sender_id in replied_users:
        return

    replied_users.add(event.sender_id)

    await event.reply(
        "ʜɪ\n\n"
        "I Aᴍ Oꜰꜰʟɪɴᴇ Aɴᴅ Cᴏᴍᴇ Oɴʟɪɴᴇ Sᴏᴏɴ "
        "Aɴᴅ Rᴇᴩʟy Yᴏᴜ 😴😴"
    )

client.start()
client.run_until_disconnected()
