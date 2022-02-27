import discord
import os
import champion

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
        
        if message.content.upper().startswith('!LOOK UP'):
            temp1 = message.content[9:12].replace(' ', '')
            temp2 = message.content[12:].replace(' ', '')
            msg = 'http://' + temp1 + '.op.gg/summoner/userName=' + temp2 + ' {0.author.mention}'.format(message)
            await message.channel.send(msg)
        
        if message.content == '!info':
            await champion.get_champion(discord, message)

        if message.content == '!counter':
            await champion.get_counter_champion(discord, message)

        if message.content.upper().startswith('!CLASSEMENT'):
            temp = message.content[11:].replace(' ', '')
            msg = 'http://' + temp + '.op.gg/leaderboards/ {0.author.mention}'.format(message)
            await message.channel.send(msg)
            

client.run(TOKEN)
