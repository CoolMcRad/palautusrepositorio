import requests
from player import Player

class PlayerReader:
    def __init__(self, address):
        self._url = address

    def get_players(self):
        response = requests.get(self._url).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players