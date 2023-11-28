import asyncio
from os import environ 
from pyrogram import Client

loop = asyncio.get_event_loop()

User = Client(
   name="userbot",
   session_string=environ["SESSION_STRING"]
)

async def main():
    await User.start()
    print(f"Successfully {User.me.first_name} started")
    await User.approve_all_chat_join_requests(chat_id=environ["CHAT_ID"])
    print("Sucessfully accepted all requests")
    await User.stop()

loop.run_until_complete(main())
