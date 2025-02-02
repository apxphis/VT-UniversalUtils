# libraries needed for main.py! :D
from os import os, getenv
from dotenv import load_dotenv

# pls generate your own token
load_dotenv()
TOKEN=os.getenv("TOKEN")

from interactions import Client, listen, Intents

bot = Client(intents=Intents.DEFAULT)

@listen
async def on_ready():
    print(f"logged in as {bot.user}! :3\n bot owner !: {bot.owner}")

bot.load_extension("exts.quote")
bot.start(TOKEN)
