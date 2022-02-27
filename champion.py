import discord
import requests
from bs4 import BeautifulSoup

async def get_champion(discord,message):
    info = champion_info()

    embed = discord.Embed(
        title="Info de Renekton",
        url="https://www.leagueoflegends.com/fr-fr/champions/renekton/"
    )

    embed.set_image(
        url=info['img']
    )

    embed.set_author(
        name= "Renekton"
    )

    await message.channel.send(embed=embed)

def champion_info():

    info = {}

    url = "https://www.leagueoflegends.com/fr-fr/champions/renekton/"

    req = requests.get(url)
    soup = BeautifulSoup(req.content, features="html.parser")

    info['img'] = soup.find("div", class_="fyyYJz").find("img")['src']

    return info

async def get_counter_champion(discord, message):

    info = counter_champion()

    embed = discord.Embed(
        title="Renekton : \n\n"
    )
    embed.add_field(name="Weak Against : \n",value=info["weak"][0:],inline=True)
    embed.add_field(name="\n\nStrong Against : \n",value=info["strong"][0:],inline=True)

    await message.channel.send(embed=embed)

def counter_champion():

    info = {}

    url = "https://www.championcounter.com/renekton"

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