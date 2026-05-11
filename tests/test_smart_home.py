import unittest
from smart_home.domain import InteligentnyDom, Lampa, Termostat, CzujnikRuchu, StatusUrzadzenia

class TestLampa(unittest.TestCase):

    def test_domyslny_status(self):
        lampa = Lampa("Lampa", "Salon")
        self.assertEqual(lampa.status, StatusUrzadzenia.WYLACZONE)

    def test_wlacz(self):
        lampa = Lampa("Lampa", "Salon")
        lampa.wlacz()
        self.assertEqual(lampa.status, StatusUrzadzenia.WLACZONE)

    def test_wylacz(self):
        lampa = Lampa("Lampa", "Salon")
        lampa.wlacz()
        lampa.wylacz()
        self.assertEqual(lampa.status, StatusUrzadzenia.WYLACZONE)

    def test_ustaw_poziom(self):
        lampa = Lampa("Lampa", "Salon")
        lampa.ustawPoziom(80.0)
        self.assertEqual(lampa.jasnosc, 80.0)


class TestTermostat(unittest.TestCase):

    def test_domyslna_temperatura(self):
        termostat = Termostat("Termostat", "Korytarz")
        self.assertEqual(termostat.temperatura, 20.0)

    def test_wlacz(self):
        termostat = Termostat("Termostat", "Korytarz")
        termostat.wlacz()
        self.assertEqual(termostat.status, StatusUrzadzenia.WLACZONE)

    def test_ustaw_poziom(self):
        termostat = Termostat("Termostat", "Korytarz")
        termostat.ustawPoziom(22.5)
        self.assertEqual(termostat.temperatura, 22.5)


class TestCzujnikRuchu(unittest.TestCase):

    def test_domyslny_wykryto_ruch(self):
        czujnik = CzujnikRuchu("Czujnik", "Przedpokój")
        self.assertFalse(czujnik.wykrytoRuch)

    def test_wlacz(self):
        czujnik = CzujnikRuchu("Czujnik", "Przedpokój")
        czujnik.wlacz()
        self.assertEqual(czujnik.status, StatusUrzadzenia.WLACZONE)

    def test_wylacz(self):
        czujnik = CzujnikRuchu("Czujnik", "Przedpokój")
        czujnik.wlacz()
        czujnik.wylacz()
        self.assertEqual(czujnik.status, StatusUrzadzenia.WYLACZONE)


class TestInteligentnyDom(unittest.TestCase):

    def test_dodaj_urzedzenie(self):
        dom = InteligentnyDom()
        lampa = Lampa("Lampa", "Salon")
        dom.dodajUrzadzenie(lampa)
        self.assertEqual(len(dom.urzadzenia), 1)

    def test_wlacz_wszystkie_przylaczalne(self):
        dom = InteligentnyDom()
        dom.dodajUrzadzenie(Lampa("Lampa", "Salon"))
        dom.dodajUrzadzenie(Termostat("Termostat", "Korytarz"))
        dom.wlaczWszystkiePrzelaczalne()
        for urzadzenie in dom.urzadzenia:
            self.assertEqual(urzadzenie.status, StatusUrzadzenia.WLACZONE)



if __name__ == "__main__":
    unittest.main()
