from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, Not, HasAtLeast, HasFewerThan, PlaysIn, All, Or

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    #First matches
    """
    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )
    """

    ## For Not
    """
    matcher = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )
    """

    ## For HasFewerThan
    """
    matcher = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )
    """
    ##For All
    #matcher = All()

    ## 1. Or-testi:
    """
    matcher = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )
    """

    ## 2. Or-testi
    matcher = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher):
        print(player)


if __name__ == "__main__":
    main()
