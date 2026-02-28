import discord
import random
import os

TOKEN = os.getenv("TOKEN")
CHANNEL_ID = int(os.getenv("CHANNEL_ID"))

livers = [
    {"name": "月ノ美兎", "image": "https://example.com/mito.png"},
    {"name": "葛葉", "image": "https://example.com/kuzuha.png"},
    {"name": "叶", "image": "https://example.com/kanae.png"}
]

class MyClient(discord.Client):
    def __init__(self):
        intents = discord.Intents.default()
        super().__init__(intents=intents)
        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.tree.sync()

client = MyClient()

@client.tree.command(name="nijisanji", description="ランダムに1人選ぶ")
async def nijisanji(interaction: discord.Interaction):
    liver = random.choice(livers)
    await interaction.response.send_message(f"{liver['name']}\n{liver['image']}")

client.run(TOKEN)
