import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(10)

    def test_luodun_kassapaatteen_rahamaara_on_oikea(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_luodun_kassapaatteen_myytyjen_lounaiden_maara_on_oikea(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_ostaminen_riittavalla_kateisella_toimii(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(vaihtoraha, 60)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_lounaan_ostaminen_ei_riittavalla_kateisella_toimii(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_lounaan_ostaminen_riittavalla_kateisella_toimii(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(vaihtoraha, 100)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_ostaminen_ei_riittavalla_kateisella_toimii(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihtoraha, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullisen_lounaan_ostaminen_riittavalla_korttisaldolla_toimii(self):
        maksukortti = Maksukortti(300)
        palautus = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 60)
        self.assertEqual(palautus, True)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_edullisen_lounaan_ostaminen_ei_riittavalla_korttisaldolla_toimii(self):
        maksukortti = Maksukortti(100)
        palautus = self.kassapaate.syo_edullisesti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(palautus, False)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaan_lounaan_ostaminen_riittavalla_korttisaldolla_toimii(self):
        maksukortti = Maksukortti(500)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(palautus, True)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_maukkaan_lounaan_ostaminen_ei_riittavalla_korttisaldolla_toimii(self):
        maksukortti = Maksukortti(2)
        palautus = self.kassapaate.syo_maukkaasti_kortilla(maksukortti)
        self.assertEqual(maksukortti.saldo, 2)
        self.assertEqual(palautus, False)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortin_lataaminen_positiivisella_maaralla_toimii(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, 100)

        self.assertEqual(maksukortti.saldo, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortin_lataaminen_negatiivisella_maaralla_toimii(self):
        maksukortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(maksukortti, -5)

        self.assertEqual(maksukortti.saldo, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
