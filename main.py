import discord
import os
import feed
from dotenv import load_dotenv

client = discord.Client()
load_dotenv()

TOKEN = os.getenv('TOKEN')
LOG_CHANNEL = int(os.getenv('LOG_CHANNEL'))
CHANNEL = int(os.getenv('CHANNEL'))


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

    if message.content == '!patch':
        await feed.get_patch_note(discord, message)


client.run(TOKEN)
