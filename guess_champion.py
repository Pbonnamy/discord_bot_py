import discord
import settings
import asyncio
import time

timeout = 10


async def guess(client):
    file = discord.File("assets/pixelated/xerath.jpg", filename="xerath.jpg")

    embed = discord.Embed(
        title='Who\'s that champion ?',
        description='Vous avez ' + str(timeout) + ' secondes'
    )

    embed.set_image(
        url="attachment://xerath.jpg"
    )

    await client.get_channel(settings.CHANNEL).send(file=file, embed=embed)

    end = time.time() + timeout

    while time.time() < end:
        try:
            msg = await client.wait_for("message", check=None, timeout=end-time.time())
        except asyncio.TimeoutError:
            break

    await client.get_channel(settings.CHANNEL).send('**Le jeu est fini, vous n\'avez pas trouvé !**')
