import discord
import settings
import feed
import database
import guess_champion
import threading
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    await client.get_channel(settings.LOG_CHANNEL).send(client.user.name + ' is **online**')
    await database.init_db(client)

    #threading.Thread(target=asyncio.run, args=(feed.get_esport_match(client),)).start()
    #threading.Thread(target=asyncio.run, args=(feed.get_patch_note(client),)).start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == settings.CHANNEL:
        if message.content == '!hello':
            await message.channel.send('Hello <@' + str(message.author.id) + '> !')

        if message.content == '!guess':
            await guess_champion.guess(client)

        if message.content == '!help':
            await settings.help(client)

client.run(settings.TOKEN)
