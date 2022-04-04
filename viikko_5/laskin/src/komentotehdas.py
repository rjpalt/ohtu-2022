import sys

class Summa:
    def laske(self, luku1, luku2):
        return luku1 + luku2

class Erotus:
    def laske(self, luku1, luku2):
        return luku1 - luku2

class Lopeta:
    def suorita():
        print('Loppu')
        sys.exit(0)

class Operaatiotehdas:
    @staticmethod
    def luo(operaatio):
        if operaatio == "summa":
            return Summa()
        elif operaatio == "tulo":
            return Tulo()

        return Erotus()

class Komentotehdas:
    def __init__(self, io):
        self.io = io

        self.komennot = {
            "summa": Summa(self.io),
            "tulo": Tulo(self.io),
            "nelio": Nelio(self.io),
            "lopeta": Lopeta(self.io)
        }

    def hae(self, komento):
        if komento in self.komennot:
            return self.komennot[komento]

        return Tuntematon(self.io)