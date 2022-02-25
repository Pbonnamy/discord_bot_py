import settings
import discord
import json
import random


async def summon(client, user_id):
    sql = "SELECT * FROM users WHERE id=" + str(user_id) + " AND points >= 1000"
    settings.DB_CURSOR.execute(sql)
    result = settings.DB_CURSOR.fetchall()

    if len(result) == 0:
        await client.get_channel(settings.CHANNEL).send('Impossible <@' + str(user_id) + '>, il te faut mininum 1000 💎.')
    else:
        champion = pick_champion()
        file = discord.File("assets/basic/" + champion['image'], filename=champion['image'])

        embed = discord.Embed(
            title='Tu as invoqué : ' + champion['name'].capitalize(),
            description='Valeur : ' + str(champion['points']) + ' 💎'
        )

        embed.set_image(
            url="attachment://" + champion['image']
        )

        await client.get_channel(settings.CHANNEL).send(file=file, embed=embed)
        handle_owned(user_id, champion['name'])


def pick_champion():
    with open("champions.json") as file:
        content = json.load(file)

        available = [champ for champ in content if champ['owned_by'] is None]

        return available[random.randint(0, len(available) - 1)]


def handle_owned(user_id, name):
    sql = "UPDATE users SET points = points-%s WHERE id=%s"
    val = (1000, user_id)

    settings.DB_CURSOR.execute(sql, val)
    settings.DB.commit()

    with open("champions.json", "r+") as file:
        content = json.load(file)
        for champion in content:
            if champion['name'] == name:
                champion['owned_by'] = user_id
        file.seek(0)
        json.dump(content, file, indent=4)
        file.truncate()
