from player import Player
from PlayerReader import PlayerReader
from PlayerStats import PlayerStats
from datetime import datetime

def main():

    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)
    stats = PlayerStats(reader)
    players = stats.top_scorers_by_nationality("FIN")

    print('Players from FIN', datetime.now(), "\n")

    for player in players:
        print(player)


main()
