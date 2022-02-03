import PlayerReader
from player import Player

class PlayerStats():

    def __init__(self, reader: 'PlayerReader'):
        
        self._reader = reader

    def top_scorers_by_nationality(self, nationality: str):


        def rank_by_points(player: 'Player') -> int:

            return (player.getPoints(), player.goals)


        players = self._reader.get_players()

        playersByNat = filter(lambda player: player.nationality == nationality, players)

        return sorted(playersByNat, key=rank_by_points, reverse=True)

