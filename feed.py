import requests
from bs4 import BeautifulSoup


async def get_patch_note(discord, message):
    info = patch_note_info()

    embed = discord.Embed(
        title="NOTES DE PATCH 12.1",
        url="https://www.leagueoflegends.com/fr-fr/news/game-updates/patch-12-1-notes/"
    )

    embed.set_image(
        url=info['img']
    )

    embed.set_author(
        name="League of Legends",
        icon_url="https://preview.redd.it/itq8rpld8va51.png?width=256&format=png&auto=webp&s=9701ba6228c29bf2d7e3dfffd45b9a3562507289"
    )

    await message.channel.send(embed=embed)


def patch_note_info():
    url = "https://www.leagueoflegends.com/fr-fr/news/game-updates/patch-12-1-notes/"
    req = requests.get(url)

    soup = BeautifulSoup(req.content, features="html.parser")

    info = {}

    info['img'] = soup.find("a", class_="cboxElement").find("img")['src']

    return info
