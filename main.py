import discord
import settings
import feed
import database

client = discord.Client()


@client.event
async def on_ready():
    await client.get_channel(settings.LOG_CHANNEL).send(client.user.name + ' is **online**')
    await database.init_db(client)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == settings.CHANNEL:
        if message.content == '!hello':
            await message.channel.send('Hello <@' + str(message.author.id) + '> !')

    if message.content == '!patch':
        await feed.get_patch_note(discord, message)


client.run(settings.TOKEN)
