###############################################
app_id = 29706540
app_hash = 'c819038d936f92ef21280db078a67337'
###############################################


import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pyrogram import Client, types

print('Иди нахуй, пока я бота запускаю')
client = Client('time_emoji_by_MrNagaron', app_id, app_hash)
client.start()
client.stop()
print('Бота запустил, но ты оставайся там же.')


async def changeEmojiTime() -> None:
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    getLines = open("./emojiIDList/" + str(hour), "r").readlines()
    me_info = await client.get_me()
    if not ((not me_info.emoji_status is None) and (me_info.emoji_status.custom_emoji_id == int(getLines[minute]))):
        await client.set_emoji_status(types.EmojiStatus(custom_emoji_id=int(getLines[minute])))


scheduler = AsyncIOScheduler()
scheduler.add_job(changeEmojiTime, "interval", seconds=10)
scheduler.start()
client.run()
