# libraries needed for main.py! :D
import os
from dotenv import load_dotenv

# pls generate your own token
load_dotenv()
TOKEN=os.getenv("TOKEN")

from interactions import Client, listen, Intents
from interactions import slash_command, SlashContext

# set up default intents
bot = Client(
    intents=Intents.DEFAULT,
    sync_interactions=True
)

# listen for start-up
@listen()
async def on_ready():
    print(f"logged in as {bot.user}! :3\n bot owner !: {bot.owner}")

# base commands that will always be loaded in the main bot.py
@slash_command(
    name="support",
    description="sends the link to the support server!",
)
async def support(ctx: SlashContext):
    await ctx.send("here's our support server link!:\nhttps://discord.ggJcBvUTVe7g")

# ping the bot
@slash_command(
    name="ping",
    description="you know what it does."
)
async def ping(ctx: SlashContext):
    await ctx.send(f"pong! {ctx.user.mention}")

bot.load_extension("exts.quote")
bot.start(TOKEN)
