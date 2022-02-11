import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):

        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)



    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)



    def test_yhden_tuotteen_lisaamisen_jalkeen_hinta_on_yhden_tuote_hinta(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)    



    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_kaksi_tuotetta_korissa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)



    def test_kahden_eri_tuotteen_ostoskorin_hinta_on_tuotteiden_hinnan_summa(self):
        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        self.assertEqual(self.kori.hinta(), 5)


    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_2_tavaraa(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)


    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korin_hinta_on_2x_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 6)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)


    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), 'Maito')
        self.assertEqual(ostos.lukumaara(), 1)


    def test_kahden_eri_tuotteen_jalkeen_korissa_on_kaksi_eri_ostosta(self):

        maito = Tuote("Maito", 3)
        leipa = Tuote("Leipä", 2)

        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(leipa)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)


    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostos(self):

        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)


    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_ostos_samalla_nimella_ja_lukumaara_kaksi(self):
        
        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].tuotteen_nimi(), 'Maito')
        self.assertEqual(ostokset[0].lukumaara(), 2)


    def test_jos_korissa_kaksi_samaa_tuotetta_ja_yksi_poistetaan_koriin_jaa_tuotetta_yksi_kappale(self):

        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(ostokset[0].tuotteen_nimi(), 'Maito')
        self.assertEqual(ostokset[0].lukumaara(), 1)


    def test_jos_korista_poistetaan_viimeinen_ostoksen_alla_oleva_tuote_ostos_poistetaan_korista_kokonaan(self):

        maito = Tuote("Maito", 3)
        
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 0)
        self.assertEqual(self.kori.hinta(), 0)