import discord
import os
import requests
import asyncio
import settings
from bs4 import BeautifulSoup

def my_split(word):
    return [char for char in word]

async def myrank(client, username):

    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
    }

    used_url = 'https://euw.op.gg/summoners/euw/' + username
    req = requests.get(used_url, headers=headers)

    soup = BeautifulSoup(req.content, features="html.parser")

    rank_tier = soup.find("div", class_="tier-rank").text
    lp = soup.find("span", class_="lp").text
    win_lose = soup.find("span", class_="win-lose").text
    rank_logo = soup.find("div", class_="medal").find("div").find("img")
    rank_logo = rank_logo['src']

    find_L = win_lose.find("L") + 1
    win_lose = my_split(win_lose)
    win_lose.insert(find_L," - ")
    win_lose = "".join(win_lose)

    win_lose = win_lose.split("-", 1)
    winrate = win_lose[1]
    win_lose = win_lose[0]

    rank = [rank_tier,lp,win_lose,winrate,rank_logo]

    most_played_champ = soup.find("div", class_="champion-box").find("div", class_="info").find("div", class_="name").find("a").text

    username = username.split('%20')
    username = " ".join(username)

    embed = discord.Embed(
        color=discord.Color.blue(),
        title='Rang de "'+username+'"',
        url=used_url,
        #description="v v v v v v",
        #description=rank[0] + " : " + rank[1] + " ----> " + rank[2],

    )

    embed.set_image(
        url=rank_logo
    )

    #embed.set_thumbnail(url=used_url)

    embed.add_field(name="Rang : ", value=rank[0], inline=True)
    embed.add_field(name="LP : ", value=rank[1], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name="Win-Lose : ", value=rank[2], inline=True)
    embed.add_field(name="Winrate : ", value=rank[3], inline=True)
    embed.add_field(name="\u200B", value="\u200B", inline=False)
    embed.add_field(name="Champion le plus joué :", value=most_played_champ, inline=False)

    #embed.set_image(
    #    url="attachment://" + champion['image']
    #)

    await client.get_channel(settings.CHANNEL).send(embed=embed)
    #return rank
