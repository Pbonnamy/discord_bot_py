import discord
import requests
from bs4 import BeautifulSoup


async def get_champion(message, name):
    info = champion_info(name)

    embed = discord.Embed(
        title="Info de "+name.capitalize(),
        url="https://www.leagueoflegends.com/fr-fr/champions/renekton/"
    )

    embed.set_image(
        url=info['img']
    )

    embed.set_author(
        name=name.capitalize()
    )

    await message.channel.send(embed=embed)


def champion_info(name):
    info = {}

    url = "https://www.leagueoflegends.com/fr-fr/champions/"+name

    req = requests.get(url)
    soup = BeautifulSoup(req.content, features="html.parser")

    info['img'] = soup.find("div", class_="fyyYJz").find("img")['src']

    return info


async def get_counter_champion(message, name):
    info = counter_champion(name)

    embed = discord.Embed(
        title=name.capitalize()+" : \n\n"
    )

    embed.add_field(name="Faible contre : \n", value='\n'.join(info["weak"]), inline=False)
    embed.add_field(name="\n\nFort contre : \n", value='\n'.join(info["strong"]), inline=False)

    await message.channel.send(embed=embed)


def counter_champion(name):
    info = {}

    url = "https://www.championcounter.com/" + name

    req = requests.get(url)
    soup = BeautifulSoup(req.content, features="html.parser")

    champions = soup.find("div", id='weakAgainst').find_all("a", class_='entity')

    info['weak'] = []

    for champion in champions:
        info['weak'].append(champion['data-name'])

    champions2 = soup.find("div", id='strongAgainst').find_all("a", class_='entity')

    info['strong'] = []

    for champion in champions2:
        info['strong'].append(champion['data-name'])

    return info
