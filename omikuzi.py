
#ライブラリを読み込む

import discord
import random
from discord.client import Client

from discord.gateway import EventListener

#起動時に必要なオブジェクト
client = discord.Client()

#起動時に動作する処理 
@client.event
async def on_ready():
    print("ログイン完了")

omikuzi = [
    "やったー、大大大大大大大大大大大大大大大大大大大大吉が出たでー" if i < 1 else
    "大吉が出たでー" if 2 <= i < 20 else
    "まぁまぁ、中吉が出たでー" if 20 <= i < 40 else
    "残念、小吉だー" if 40 <= i < 70 else
    "運勢悪いでー、凶がでた……" for i in range (71) ]

#おみくじの返事
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('おみくじ'):
        await message.channel.send(omikuzi[random.randrange(len(omikuzi))])

client.run('トークン')