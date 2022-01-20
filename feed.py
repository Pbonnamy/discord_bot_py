async def get_patch_note(discord, message):
    embed = discord.Embed(
        title="NOTES DE PATCH 12.1",
        url="https://www.leagueoflegends.com/fr-fr/news/game-updates/patch-12-1-notes/"
    )

    embed.set_image(
        url="https://images.contentstack.io/v3/assets/blt731acb42bb3d1659/blt021e5a00ec591880/61d47d0595cb603e6b5ce067/LOL_12.1-Infographic_1920x1080_JCao_v05_FR.jpg"
    )

    embed.set_author(
        name="League of Legends",
        icon_url="https://preview.redd.it/itq8rpld8va51.png?width=256&format=png&auto=webp&s=9701ba6228c29bf2d7e3dfffd45b9a3562507289"
    )

    await message.channel.send(embed=embed)
