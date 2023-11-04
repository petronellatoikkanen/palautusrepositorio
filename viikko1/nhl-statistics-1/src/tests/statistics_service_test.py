
import unittest
from statistics_service import StatisticsService, SortBy
from player import Player
from player_reader import PlayerReaderStub
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

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

    def test_pelaajat_oikeassa_jarjestyksessa(self):
        top = []
        for player in self.stats.top(5, 1):
            top.append(player.name)
        
        tops = ['Gretzky', 'Lemieux', 'Yzerman', 'Kurri', 'Semenko']

        self.assertEqual(top, tops)

    def test_pelaajat_oikeassa_jarjestyksessa_goals(self):
        top = []
        for player in self.stats.top(5, 2):
            top.append(player.name)
        
        tops = ['Lemieux', 'Yzerman', 'Kurri', 'Gretzky', 'Semenko']

        self.assertEqual(top, tops)

    def test_pelaajat_oikeassa_jarjestyksessa_assists(self):
        top = []
        for player in self.stats.top(5, 3):
            top.append(player.name)
        
        tops = ['Gretzky', 'Yzerman', 'Lemieux', 'Kurri', 'Semenko']

        self.assertEqual(top, tops)

    def test_pelaajat_oikeassa_jarjestyksessa_ei_kriteeria(self):
        top = []
        for player in self.stats.top(5):
            top.append(player.name)
        
        tops = ['Gretzky', 'Lemieux', 'Yzerman', 'Kurri', 'Semenko']

        self.assertEqual(top, tops)

    def test_palauttaa_None_jos_ei_ole_pelaajaa (self):
        self.assertEqual(self.stats.search("å"), None)

    def test_hakee_oikean_pelaajan(self):
        self.assertEqual(self.stats.search("Lemieux").name, "Lemieux")

    def test_hakee_oikean_tiimin_pelaajat(self):
        tiimi = "PIT"

        self.assertEqual(self.stats.team("PIT")[0].name, "Lemieux")

    