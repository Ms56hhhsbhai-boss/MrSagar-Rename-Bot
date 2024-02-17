import asyncio
from pyrogram import Client, compose,idle
import os

from plugins.cb_data import app as Client2

TOKEN = os.environ.get("TOKEN", "6763008780:AAHstGsyGIx4L6mmbcQ44LVu5jR4JI9nIxM")

API_ID = int(os.environ.get("API_ID", "14350423"))

API_HASH = os.environ.get("API_HASH", "838b0b81758d276215b3647821b707ad")

STRING = os.environ.get("STRING", "BQDa-FcArN0es1ym8cEUB36r7jYyQQ66D8-niIPZ_Tp5mjuVNcTX6hmqqoOIkFNKaFu6Ir-_F_1TMFodn3FcBkB8w9fVyzF6XGU13jQ0lrsGdhUbtBVbTMnJRoCQc7_8WAJZ2zmr46h1u9EzjoNDLWrGGz-vIRnEPIkR7FTgxiHnkefwAkbIPdpZiQzmkZ_NbMNaxHeGp2ohecFeSQllovrwJrN-7bKqnbdmxlaNdBVM92ZvaIhO4qagRS30vaNB9W2EZEi6SHt5a5xgAUoxwPIJzs5u75vIy1YXZkK3ErsxRJy0yAupLW_0ANdMjg7yfq6uzmIhhuj7Z3LsQy-d4jmK2Z08wAAAAAGJzmhsAA")


bot = Client(

           "Renamer",

           bot_token=TOKEN,

           api_id=API_ID,

           api_hash=API_HASH,

           plugins=dict(root='plugins'))
           

if STRING:
    apps = [Client2,bot]
    for app in apps:
        app.start()
    idle()
    for app in apps:
        app.stop()
    
else:
    bot.run()
