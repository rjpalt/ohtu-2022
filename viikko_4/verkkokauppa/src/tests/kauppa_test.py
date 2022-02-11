import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        self.tuote1 = 10
        self.tuote2 = 20
        self.tuote3 = 0

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):

            if tuote_id == 1:
                self.tuote1 = self.tuote1 - 1
                return self.tuote1
            if tuote_id == 2:
                self.tuote2 = self.tuote2 - 1
                return self.tuote2
            if tuote_id == 3:
                self.tuote3 = self.tuote3 - 1
                return self.tuote3

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 2)
            if tuote_id == 3:
                return Tuote(3, "banaani", 1)

        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote
        self.varasto_mock.saldo.side_effect = varasto_saldo

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    
    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", "33333-44455", 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista


    def test_osta_kaksi_eri_tuotetta_varmista_oston_oikeellisuus(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("Rasmus", "858585")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("Rasmus", 42, "858585", "33333-44455", 7)


    def test_osta_kaksi_samaa_tuotetta_varmista_oston_oikeellisuus(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("Rasmus", "858585")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("Rasmus", 42, "858585", "33333-44455", 4)


    def test_ostos_saldollisella_ja_saldottomalla_tuotteella_varmista_ostoksen_oikeus(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("Rasmus", "858585")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("Rasmus", 42, "858585", "33333-44455", 2)

    def test_aloita_asiointi_nollaa_ostoskorin(self):

        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("Rasmus", "858585")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("Rasmus", 1, "858585", "33333-44455", 2)

        # tehdään toiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("Rasmus", "858585")

        self.pankki_mock.tilisiirto.assert_called_with("Rasmus", 2, "858585", "33333-44455", 7)

    def test_korista_poistaminen_toimii(self):

        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("Rasmus", "858585")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("Rasmus", 42, "858585", "33333-44455", 5)

        # tehdään toiset ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("Rasmus", "858585")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("Rasmus", 42, "858585", "33333-44455", 4)