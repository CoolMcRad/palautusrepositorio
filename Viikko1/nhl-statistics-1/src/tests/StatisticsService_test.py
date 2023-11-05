import unittest
from statistics_service import StatisticsService
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

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_palauttaa_oikean_pelaajan(self): 
        self.assertAlmostEqual(self.stats.search("Semenko").name, "Semenko")

    def test_search_palauttaa_none_jos_pelaajaa_ei_ole(self): 
        self.assertAlmostEqual(self.stats.search("Selänne"), None)

    def test_team_palauttaa_joukkueen_pelaajat(self): 
        self.assertAlmostEqual(self.stats.team("EDM")[1].name, "Kurri")

    def test_top_palauttaa_oikein(self): 
        self.assertAlmostEqual(self.stats.top(1)[0].name, "Gretzky")
