import discord
import random
import os
from discord.ext import tasks
from datetime import datetime
import zoneinfo

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

livers = [
    {"name": "月ノ美兎", "image": "https://example.com/mito.png"},
    {"name": "葛葉", "image": "https://example.com/kuzuha.png"},
    {"name": "叶", "image": "https://example.com/kanae.png"}
]

intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Bot起動完了")
    send_random.start()

@tasks.loop(minutes=1)
async def send_random():
    now = datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))
    if now.hour == 19 and now.minute == 0:
        liver = random.choice(livers)
        channel = client.get_channel(CHANNEL_ID)
        await channel.send(liver["name"])
        await channel.send(liver["image"])

client.run(TOKEN)
