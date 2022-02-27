import discord
import settings
import feed
import database
import guess_champion
import summon_champion
import champion
import champion_stats

client = discord.Client()


@client.event
async def on_ready():
    await client.get_channel(settings.LOG_CHANNEL).send(client.user.name + ' is **online**')
    await database.init_db(client)

    client.loop.create_task(feed.get_esport_match(client))
    client.loop.create_task(feed.get_patch_note(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == settings.CHANNEL:
        if message.content == '!hello':
            await message.channel.send('Hello <@' + str(message.author.id) + '> !')

        if message.content.startswith('!info'):
            name = message.content.split(' ')[1]
            await champion_stats.get_champion(message, name)

        if message.content.startswith('!counter'):
            name = message.content.split(' ')[1]
            await champion_stats.get_counter_champion(message, name)

        if message.content == '!guess':
            await guess_champion.guess(client)

        if message.content == '!help':
            await settings.help(client)

        if message.content == '!summon':
            await summon_champion.summon(client, message.author.id)

        if message.content == '!reset':
            await champion.reset(client)

        if message.content.startswith('!sell'):
            name = message.content.split(' ')[1]
            await summon_champion.sell(client, name, message.author.id)

        if message.content == '!list':
            await summon_champion.champion_list(client, message.author.id)


client.run(settings.TOKEN)
