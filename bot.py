import requests
import time
import os
from telegram import Bot

BOT_TOKEN = os.getenv("7742565613:AAGIiXAHyeO-1DGAJwhDy31vc7BhlLUvEfg")
CHAT_ID = os.getenv("6978546449")

bot = Bot(token=BOT_TOKEN)

URL = "https://hiring.amazon.ca/app#/jobSearch"

last_text = ""

def check():
    global last_text
    
    headers = {"User-Agent": "Mozilla/5.0"}
    r = requests.get(URL, headers=headers)
    
    if "St. Thomas" in r.text:
        if r.text != last_text:
            bot.send_message(
                chat_id=CHAT_ID,
                text="🔥 ST THOMAS SHIFT UPDATE! CHECK NOW!"
            )
            last_text = r.text

while True:
    check()
    time.sleep(30)
