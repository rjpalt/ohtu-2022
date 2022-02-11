from tuote import Tuote
from ostos import Ostos
from functools import reduce

class Ostoskori:
    def __init__(self):
        
        self._tuotteet = []
        self._hinta = 0

    def tavaroita_korissa(self):

        if len(self._tuotteet) == 0:
            return 0
        else:
            return reduce(lambda summa, ostos: summa + ostos.lukumaara(), self._tuotteet, 0)


    def hinta(self):

        if len(self._tuotteet) == 0:
            return 0
        else:
            return reduce(lambda summa, ostos: summa + ostos.hinta(), self._tuotteet, 0)


    def lisaa_tuote(self, lisattava: Tuote):

        for ostos in self._tuotteet:
            if ostos.tuotteen_nimi() == lisattava.nimi():
                print('Muutetaan')
                ostos.muuta_lukumaaraa(1)
                return

        self._tuotteet.append(Ostos(lisattava))
        self._hinta += lisattava._hinta

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        pass
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
