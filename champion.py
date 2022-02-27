import json
import random
import settings


def rand_available():
    with open("champions.json") as file:
        content = json.load(file)
        available = [champ for champ in content if champ['owned_by'] is None]

        if len(available) == 0:
            raise Exception('No champion available.')
        else:
            return Champion(available[random.randint(0, len(available) - 1)]['name'])


def rand_champion():
    with open("champions.json") as file:
        content = json.load(file)
        return Champion(content[random.randint(0, len(content) - 1)]['name'])


async def reset(client):
    with open("champions.json") as file:
        content = json.load(file)
        for champ in content:
            if champ['owned_by'] is not None:
                Champion(champ['name']).owned_by = None

    await client.get_channel(settings.CHANNEL).send('Champions possédés remis à zéro')


class Champion:
    def __init__(self, name):
        with open("champions.json") as file:
            found = False
            content = json.load(file)
            for champion in content:
                if champion['name'] == name:
                    self.name = champion['name']
                    self.image = champion['image']
                    self.points = champion['points']
                    self.owned_by = champion['owned_by']
                    found = True

            if not found:
                raise Exception('Champion not found.')

    def set_owned_by(self, owned_by):
        with open("champions.json", "r+") as file:
            content = json.load(file)
            for champion in content:
                if champion['name'] == self.name:
                    champion['owned_by'] = owned_by
            file.seek(0)
            json.dump(content, file, indent=2)
            file.truncate()
        self._owned_by = owned_by

    def get_owned_by(self):
        return self._owned_by

    owned_by = property(get_owned_by, set_owned_by)