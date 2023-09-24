import asyncio
from pyrogram import filters, enums
from pyrogram.errors import FloodWait, PeerFlood
from pyrogram.client import  Client


api_id:int
api_hash:str
with open("api_ids", "r") as api_conf:
    api_id = int(api_conf.readline().strip())
    api_hash = api_conf.readline().strip()

app = Client("my_account", api_id=api_id, api_hash=api_hash)

@app.on_message(filters.command("get_id", prefixes=".") & filters.me)
async def getid(client, message):
    print(message.chat.id)
    await message.delete(message)
    
# type .gu in chat to collect all the non admin and non bot users
@app.on_message(filters.command("gu", prefixes=".") & filters.me)
async def getAllUsers(client, message):
    msg = message
    await message.delete(message)
    open('user_ids.txt', 'w').close()
    # clear the file

    with open("user_ids.txt", "w", encoding="utf8") as file:
        async for member in app.get_chat_members(msg.chat.id):
            if member.status == enums.ChatMemberStatus.ADMINISTRATOR or member.status == enums.ChatMemberStatus.OWNER or member.user.is_bot: continue
            file.write(str(member.user.id) + "\n")
            print(f"collected user {member.user.id}:{member.user.username}")


# type this after you typed .gu
# it will send messages to all the users collected by gu
# the message content is in the file msg_text.txt
@app.on_message(filters.command("sp", prefixes=".") & filters.me)
async def startSpam(client, message):
    chat_id:int = message.chat.id
    await message.delete(message)
    userList:list[int] = []
    with open("user_ids.txt", "r", encoding="utf8") as file:
        for x in file.readlines():
            userList.append(int(x.strip("\n ")))

    spam_msg:str 
    with open("msg_text.txt", "r", encoding="utf8") as file:
        spam_msg = "\n".join(file.readlines())

    try:
        for chat_id in userList:
            try:
                await app.send_message(chat_id=chat_id, text=spam_msg)
                userList.remove(chat_id)
            except FloodWait as e:
                print(f"bot stopped for {e.value}s")
                await asyncio.sleep(e.value)

            # TODO: this doesn't work and even throws another error at e.value
            # except PeerFlood as e:
            #     print(f"bot stopped for {e.value}s")
            #     await asyncio.sleep(e.value)

            except Exception as e:
                print(f"couldn't send message to user {chat_id}")
                raise e
    finally:
        # remove users that received the message from the file
        with open("user_ids.txt", "w") as file:
            for x in userList:
                file.write(str(x) + "\n")


print("bot started")
app.run()
