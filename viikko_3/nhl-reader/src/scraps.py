"""
    url = "https://nhlstatisticsforohtu.herokuapp.com/players"
    reader = PlayerReader(url)

    players = []

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

        players.append(player)

    natPlayers = filterByNat('FIN', players)

    printPlayers = rankkaa_pisteet(natPlayers)

    for player in printPlayers:
        print(player)
"""