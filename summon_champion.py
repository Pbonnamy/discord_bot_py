import settings
import discord
import json
import champion


async def summon(client, user_id):
    sql = "SELECT * FROM users WHERE id=" + str(user_id) + " AND points >= 1000"
    settings.DB_CURSOR.execute(sql)
    result = settings.DB_CURSOR.fetchall()

    if len(result) == 0:
        await client.get_channel(settings.CHANNEL).send(
            'Impossible <@' + str(user_id) + '>, il te faut mininum 1000 💎.')
    else:
        try:
            champ = champion.rand_available()
        except:
            await client.get_channel(settings.CHANNEL).send('Impossible <@' + str(user_id) + '>, il n\'y a plus de champion disponible.')
            return


        file = discord.File("assets/basic/" + champ.image, filename=champ.image)

        embed = discord.Embed(
            title='Tu as invoqué : ' + champ.name.capitalize(),
            description='Valeur : ' + str(champ.points) + ' 💎'
        )

        embed.set_image(
            url="attachment://" + champ.image
        )

        await client.get_channel(settings.CHANNEL).send(file=file, embed=embed)

        sql = "UPDATE users SET points = points-%s WHERE id=%s"
        val = (1000, user_id)

        settings.DB_CURSOR.execute(sql, val)
        settings.DB.commit()

        champ.owned_by = user_id


async def sell(client, name, user_id):

    try:
        champ = champion.Champion(name)
    except:
        await client.get_channel(settings.CHANNEL).send('Ce champion n\'existe pas, <@' + str(user_id) + '>')
        return

    if champ.owned_by == user_id:
        sql = "UPDATE users SET points = points+%s WHERE id=%s"
        val = (champ.points, user_id)
        settings.DB_CURSOR.execute(sql, val)
        settings.DB.commit()

        champ.owned_by = None

        await client.get_channel(settings.CHANNEL).send( 'Tu as vendu ' + champ.name + ' pour ' + str(champ.points) + ' 💎, <@' + str(user_id) + '>')
    else:
        await client.get_channel(settings.CHANNEL).send('Tu ne possède pas ce champion, <@' + str(user_id) + '>')


async def champion_list(client, user_id):
    with open("champions.json") as file:
        content = json.load(file)

        champions = '\u200b'
        for champ in content:
            if champ['owned_by'] == user_id:
                champions += '**' + champ['name'] + '** ' + str(champ['points']) + ' 💎\n'

        embed = discord.Embed(
            title='Champions possédés',
        )

        embed.add_field(
            name='\u200b',
            value=champions,
            inline=False
        )

        sql = "SELECT points FROM users WHERE id=" + str(user_id);
        settings.DB_CURSOR.execute(sql)
        result = settings.DB_CURSOR.fetchall()

        points = 0

        if len(result) != 0:
            points = result[0][0]

        embed.add_field(
            name='\u200b',
            value='```' + str(points) + ' 💎 possédés```',
            inline=False
        )

        await client.get_channel(settings.CHANNEL).send(embed=embed)
