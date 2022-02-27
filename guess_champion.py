import discord
import settings
import asyncio
import time
import champion


def check(msg):
    return msg.channel.id == settings.CHANNEL


async def guess(client):
    timeout = 10

    champ = champion.rand_champion()

    file = discord.File("assets/pixelated/" + champ.image, filename=champ.image)  # pixéliser 20

    embed = discord.Embed(
        title='Who\'s that champion ?',
        description='Vous avez ' + str(timeout) + ' secondes'
    )

    embed.set_image(
        url="attachment://" + champ.image
    )

    await client.get_channel(settings.CHANNEL).send(file=file, embed=embed)

    end = time.time() + timeout
    win = False

    while time.time() < end and win is not True:
        try:
            msg = await client.wait_for("message", check=check, timeout=end - time.time())

            if msg.content == champ.name:
                await msg.add_reaction('✅')

                await client.get_channel(settings.CHANNEL).send(
                    '**Bien joué <@' + str(msg.author.id) + '>, tu as gagné ' + str(champ.points) + ' 💎 !**')
                handle_points(msg.author.id, champ.points)
                win = True
            else:
                await msg.add_reaction('❌')
        except asyncio.TimeoutError:
            break

    if not win:
        await client.get_channel(settings.CHANNEL).send('**Le jeu est fini, vous n\'avez pas trouvé !**')


def handle_points(id, points):
    sql = "INSERT INTO users (id, points) VALUES(%s, %s) ON DUPLICATE KEY UPDATE points=points+%s"
    val = (id, points, points)

    settings.DB_CURSOR.execute(sql, val)
    settings.DB.commit()
