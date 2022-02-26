import discord
import os
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

client = discord.Client()
load_dotenv()

TOKEN = os.getenv('TOKEN')
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL'))
CHANNEL = int(os.getenv('CHANNEL'))

req = requests.get('https://euw.op.gg/champions')
soup = BeautifulSoup(req.content, features="html.parser")

res = soup.find("div", id="top-banner-ad")
print(res)


@client.event
async def on_ready():
    await client.get_channel(LOG_CHANNEL).send(client.user.name + ' is **online**')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == CHANNEL:
        if message.content == '!hello':
            await message.channel.send('Hello <@' + str(message.author.id) + '> !')

client.run(TOKEN)
