import unittest
from maksukortti import Maksukortti


class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(10)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(15)
        self.assertEqual(self.maksukortti.saldo, 25)

    def test_saldo_vahenee_oikein_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5)
        self.assertEqual(self.maksukortti.saldo, 5)

    def test_saldo_vahenee_oikein_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(15)
        self.assertEqual(self.maksukortti.saldo, 10)

    def test_metodi_palauttaa_true_jos_rahat_riittavat(self):
        palautus = self.maksukortti.ota_rahaa(5)
        self.assertEqual(palautus, True)

    def test_metodi_palauttaa_false_jos_rahat_eivat_riita(self):
        palautus = self.maksukortti.ota_rahaa(15)
        self.assertEqual(palautus, False)

    def test_merkkijonon_muodostaminen_toimii_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 0.1")
