import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    ##Search function tests

    def test_return_correct_player(self):

        player = self.statistics.search("Kurri")

        self.assertAlmostEqual(str(player), "Kurri EDM 37 + 53 = 90")

    def test_return_none_for_nonexistent(self):

        player = self.statistics.search("Tikkanen")

        self.assertAlmostEqual(player, None)




    ## Team function tests

    def test_team_with_true_info(self):

        player_list = self.statistics.team('EDM')

        self.assertEqual(len(player_list), 3)

    def test_team_with_false_info(self):

        player_list = self.statistics.team('CHI')

        self.assertEqual(len(player_list), 0)

    
    
    ## Top Scorers function tests

    def test_top_scorers(self):

        result_list = self.statistics.top_scorers(3)

        self.assertAlmostEqual(len(result_list), 4)
        self.assertAlmostEqual(str(result_list[0]), "Gretzky EDM 35 + 89 = 124")