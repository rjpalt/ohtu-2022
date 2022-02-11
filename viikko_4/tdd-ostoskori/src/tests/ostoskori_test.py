import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)


# Laajenna testiä siten että se testaa myös tavaroiden määrän 
# (metodin tavaroita_korissa paluuarvo). Kun testi on valmis, 
# ohjelmoi ostoskoria sen verran että testi menee läpi. 
# Tee ainoastaan minimaalisin mahdollinen toteutus, jolla 
# saat testin läpi.

#Lisää ja commitoi muutokset ja anna kuvaava commit-viesti.