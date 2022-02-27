## Bot Discord : League of Legends

---

### Sujet validé :

- **Feed d'actualités**
  - (ex : patchnote/esport...)
- **Statistiques/classement**
  - (ex : joueurs...)
- **Mini jeu**
  - (ex : who's that champion / gacha (collectionner les champions)...)

---

### Structure du .env

- TOKEN="your_token"
- CHANNEL=your_command_channel
- LOG_CHANNEL=your_log_channel
- FEED_CHANNEL=your_feed_channel
- DB_HOST="your_db_host"
- DB_USER="your_db_user"
- DB_PWD="your_db_password"
- DB_NAME="your_db_name"

---

### Répartition des taches

### Pierre :
- Intégration de la base de donnée
- Feed de patchnote
- Feed de match esport
- Mini jeu "who's that champion ?"
  - commande ```!guess``` ➔ lance le quizz
- Mini jeu Gacha (invocation de champion)
  - commande ```!summon``` ➔ invoque un champion
  - commande ```!list``` ➔ liste les champions de l'utilisateur
  - commande ```!sell <champion>``` ➔ vends un champion possédé
  - commande ```!rest``` ➔ remet à zéro les possession de champion
- Commande ```!help``` pour référencer les commandes existantes

### Tianqi :
- Statistiques d'un champion
  - commande ```!info``` ➔ info du champion
  - commande ```!counter``` ➔ liste les champions de counter

---

### Ressources utilisées

Librairies :
  - discord.py ➔ https://discordpy.readthedocs.io/en/stable/
  - beautifulSoup ➔ https://www.crummy.com/software/BeautifulSoup/bs4/doc/
  - asyncio ➔ https://docs.python.org/fr/3/library/asyncio.html
  - json ➔ https://docs.python.org/3/library/json.html
  - mysql.connector ➔ https://dev.mysql.com/doc/connector-python/en/
  - dotenv ➔ https://pypi.org/project/python-dotenv/
  - requests ➔ https://fr.python-requests.org/en/latest/

Ressources de scraping :
  - https://guesschamp.com/league-of-legends/ ➔ assets des champions
  - https://www.leagueoflegends.com/fr-fr/news/tags/patch-notes/ ➔ patchnotes
  - https://www.esportsbet.io/stats/matches/lol/Global ➔ matchs esport

Autres ressources:
  - https://stackoverflow.com/
  - https://www.w3schools.com/python/python_mysql_getstarted.asp

--- 

- lien du dépot : https://github.com/Pbonnamy/discord_bot_py

