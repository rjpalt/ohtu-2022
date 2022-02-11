from tuote import Tuote
from ostos import Ostos
from functools import reduce

class Ostoskori:
    def __init__(self):
        
        self._tuotteet = []

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
                ostos.muuta_lukumaaraa(1)
                return

        self._tuotteet.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):

        ostokset = filter(lambda ostos : ostos.tuotteen_nimi() == poistettava.nimi(), self._tuotteet)

        ostos = None

        for osto in ostokset:
            ostos = osto
        
        if ostos.lukumaara() <= 1:
            self._tuotteet = [purchase for purchase in self._tuotteet if ostos.tuotteen_nimi() != poistettava.nimi()]
        else:
            ostos.muuta_lukumaaraa(-1)

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        
        return self._tuotteet

