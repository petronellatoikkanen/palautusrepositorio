from enum import Enum
from tkinter import ttk, constants, StringVar
import Sovelluslogiikka

class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Komentotehdas:
    def __init__(self, io):
        self.io = io

        self.komennot = {
            "Summa": Sovelluslogiikka.plus(self.io),
            "Erotus": Sovelluslogiikka.miinus(self.io),
            "Nollaus": Sovelluslogiikka.nollaa(self.io),
        }

    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]

