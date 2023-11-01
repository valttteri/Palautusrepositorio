import unittest
from statistics_service import StatisticsService
from player import Player
from sortby import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_valid_search(self):
        player = self.stats.search("Kurri")

        self.assertEqual(player.name, "Kurri")
        self.assertEqual(player.team, "EDM")
        self.assertEqual(player.goals, 37)
        self.assertEqual(player.assists, 53)

    def test_invalid_search(self):
        self.assertIsNone(self.stats.search("Selanne"))
    
    def test_team_returns_correct_players(self):
        players = self.stats.team("EDM")

        self.assertEqual(len(players), 3)
        self.assertEqual(players[0].name, "Semenko")
        self.assertEqual(players[1].name, "Kurri")
        self.assertEqual(players[2].name, "Gretzky") 
    
    def test_top_players_orderbypoints(self):
        players_ranked = self.stats.top(5, SortBy.POINTS)
        self.assertEqual(len(players_ranked), 5)
        self.assertEqual(players_ranked[0].points, 89+35)
        self.assertEqual(players_ranked[1].points, 45+54)
        self.assertEqual(players_ranked[2].points, 42+56)
        self.assertEqual(players_ranked[3].points, 37+53)
        self.assertEqual(players_ranked[4].points, 4+12)
    
    def test_top_players_orderbygoals(self):
        players_ranked = self.stats.top(5, SortBy.GOALS)
        self.assertEqual(len(players_ranked), 5)
        self.assertEqual(players_ranked[0].goals, 45)
        self.assertEqual(players_ranked[1].goals, 42)
        self.assertEqual(players_ranked[2].goals, 37)
        self.assertEqual(players_ranked[3].goals, 35)
        self.assertEqual(players_ranked[4].goals, 4)
    
    def test_top_players_orderbyassists(self):
        players_ranked = self.stats.top(5, SortBy.ASSISTS)
        self.assertEqual(len(players_ranked), 5)
        self.assertEqual(players_ranked[0].assists, 89)
        self.assertEqual(players_ranked[1].assists, 56)
        self.assertEqual(players_ranked[2].assists, 54)
        self.assertEqual(players_ranked[3].assists, 53)
        self.assertEqual(players_ranked[4].assists, 12)
