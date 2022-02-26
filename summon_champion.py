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
        if champion is not None:
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
        else:
            await client.get_channel(settings.CHANNEL).send('Impossible <@' + str(user_id) + '>, il n\'y a plus de champion disponible.')


def pick_champion():
    with open("champions.json") as file:
        content = json.load(file)

        available = [champ for champ in content if champ['owned_by'] is None]

        if len(available) == 0:
            return None
        else:
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
        json.dump(content, file, indent=2)
        file.truncate()


async def reset(client):
    with open("champions.json", "r+") as file:
        content = json.load(file)
        for champion in content:
            if champion['owned_by'] is not None:
                champion['owned_by'] = None
        file.seek(0)
        json.dump(content, file, indent=2)
        file.truncate()

    await client.get_channel(settings.CHANNEL).send('Champions possédés remis à zéro')


async def sell(client, name, user_id):
    with open("champions.json", "r+") as file:
        content = json.load(file)
        sold = False
        for champion in content:
            if champion['name'] == name and champion['owned_by'] == user_id:
                champion['owned_by'] = None
                file.seek(0)
                json.dump(content, file, indent=2)
                file.truncate()

                sql = "UPDATE users SET points = points+%s WHERE id=%s"
                val = (champion['points'], user_id)
                settings.DB_CURSOR.execute(sql, val)
                settings.DB.commit()

                sold = True
                await client.get_channel(settings.CHANNEL).send('Tu as vendu '+champion['name']+' pour '+str(champion['points'])+' 💎, <@' + str(user_id) + '>')
        if not sold:
            await client.get_channel(settings.CHANNEL).send('Tu ne possède pas ce champion, <@' + str(user_id) + '>')

