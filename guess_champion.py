import discord
import settings
import asyncio
import time
import json
import random

timeout = 10


async def guess(client):
    champion = pick_champion()

    file = discord.File("assets/pixelated/"+champion['image'], filename=champion['image'])  # pixéliser 20

    embed = discord.Embed(
        title='Who\'s that champion ?',
        description='Vous avez ' + str(timeout) + ' secondes'
    )

    embed.set_image(
        url="attachment://"+champion['image']
    )

    await client.get_channel(settings.CHANNEL).send(file=file, embed=embed)

    end = time.time() + timeout
    win = False

    while time.time() < end:
        try:
            msg = await client.wait_for("message", check=None, timeout=end - time.time())

            if msg.content == champion['name']:
                await msg.add_reaction('✅')
                await client.get_channel(settings.CHANNEL).send('**Bien joué, vous gagnez ' + str(champion['points']) + ' points !**')
                win = True
            else:
                await msg.add_reaction('❌')
        except asyncio.TimeoutError:
            break

    if not win:
        await client.get_channel(settings.CHANNEL).send('**Le jeu est fini, vous n\'avez pas trouvé !**')


def pick_champion():
    with open("champions.json") as file:
        content = json.load(file)
        return content[random.randint(0, len(content)-1)]
