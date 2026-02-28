import discord
import random
import os
from discord.ext import tasks
from datetime import datetime, time
import zoneinfo

TOKEN = os.getenv("MTQ3NzE4MDcxNzQ1NTc2OTczMw.GiLpT3.dJW-1ffHWmOxUWZveLZSQ9cKfD7siRea9tCf98")
CHANNEL_ID = int(os.getenv("1477181896885665805"))

livers = [
    {
        "name": "月ノ美兎",
        "image": "https://static.wikia.nocookie.net/virtualyoutuber/images/7/7e/Tsukino_Mito_-_Profile_Image.png"
    },
    {
        "name": "葛葉",
        "image": "https://static.wikia.nocookie.net/virtualyoutuber/images/4/4f/Kuzuha_-_Profile_Image.png"
    },
    {
        "name": "叶",
        "image": "https://static.wikia.nocookie.net/virtualyoutuber/images/2/2d/Kanae_-_Profile_Image.png"
    },
     {"name": "剣持刀也", "image": "https://static.wikia.nocookie.net/virtualyoutuber/images/0/0e/Kenzaki_Touya_-_Profile_Image.png"},
     {"name": "樋口楓", "image": "https://nijisanji.miraheze.org/images/8/8f/Higuchi_Kaede_Profile.png"},
     {"name": "社築", "image": "https://nijisanji.miraheze.org/images/7/7a/Yashiro_Kizuku_Profile.png"},
     {"name": "不破湊", "image": "https://nijisanji.miraheze.org/images/9/9d/Fuwa_Minato_Profile.png"},
     {"name": "加賀美ハヤト", "image": "https://nijisanji.miraheze.org/images/1/1e/Kagami_Hayato_Profile.png"},
intents = discord.Intents.default()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot起動完了: {client.user} (ID: {client.user.id})")
    send_random.start()


@tasks.loop(time=time(19, 0), count=None) 
async def send_random():
    now = datetime.now(zoneinfo.ZoneInfo("Asia/Tokyo"))
    print(f"タスク実行チェック: {now.strftime('%Y-%m-%d %H:%M:%S')}") 
    liver = random.choice(livers)
    channel = client.get_channel(CHANNEL_ID)

    try:
        embed = discord.Embed(
            title="19時のおすすめライバー",
            description=f"**{liver['name']}** が今日の推しです！💜",
            color=0xff69b4  # ピンク系で可愛く
        )
        embed.set_image(url=liver["image"])
        embed.set_footer(text=f"にじさんじランダム | {now.strftime('%Y/%m/%d')}")
        
        await channel.send(embed=embed)
        print(f"送信完了: {liver['name']}")
    except discord.HTTPException as e:
        print(f"送信エラー: {e}")



@send_random.before_loop
async def before_send():
    await client.wait_until_ready()
    print("send_random タスク開始待機中...")


client.run(TOKEN)
