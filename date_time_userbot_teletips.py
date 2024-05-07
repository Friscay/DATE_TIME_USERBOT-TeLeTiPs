#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
#You are free to use this code in any of your project, but you MUST include the following in your README.md (Copy & paste)
# ##Credits - [DATE_TIME Telegram userbot by TeLe TiPs] (https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs)

# Changing the code is not allowed! Read GNU AFFERO GENERAL PUBLIC LICENSE: https://github.com/teletips/DATE_TIME_USERBOT-TeLeTiPs/blob/main/LICENSE

from pyrogram import Client, filters
from pyrogram.errors import FloodWait
from lists_teletips.randompp import *
import datetime
import pytz
import asyncio
import random
import os

loop = asyncio.get_event_loop_policy()
event_loop = loop.get_event_loop()

Date_Time_Userbot = Client(
    name = "date_time_userbot_teletips",
    api_id = int(os.environ["API_ID"]),
    api_hash = os.environ["API_HASH"],
    session_string = os.environ["SESSION_STRING"]
)

Time_Zone = os.environ["TIME_ZONE"]

async def main_teletips():
    try:
        if Date_Time_Userbot.is_connected:
            pp = random.choice(randompp)
            TimeZone_teletips = datetime.datetime.now(pytz.timezone(Time_Zone))
            Time_teletips = TimeZone_teletips.strftime("%I:%M %p")
            Date_teletips = TimeZone_teletips.strftime("%b %d")
            await Date_Time_Userbot.set_profile_photo(pp)
            me = await Date_Time_Userbot.get_me()
            photos = await Date_Time_Userbot.get_profile_photos("me")
            try:
                await Date_Time_Userbot.delete_profile_photos(photos[1].file_id)
            except Exception:
                pass        
            print("Profile Updated!")
        await asyncio.sleep(60)     
except FloodWait as e:
    await asyncio.sleep(e.x)         

print("DATE TIME USERBOT IS ALIVE!")
asyncio.run(main_teletips())

#Copyright ©️ 2021 TeLe TiPs. All Rights Reserved
