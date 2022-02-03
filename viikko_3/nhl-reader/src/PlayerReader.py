import requests
from player import Player

class PlayerReader:

    def __init__(self, url):
        
        self._url = url
        self._players = []

    def get_players(self):

        response = requests.get(self._url).json()

        for player_dict in response:
            player = Player(
                player_dict['name'],
                player_dict['nationality'],
                player_dict['assists'],
                player_dict['goals'],
                player_dict['penalties'],
                player_dict['team'],
                player_dict['games']
            )

            self._players.append(player)

        return self._players