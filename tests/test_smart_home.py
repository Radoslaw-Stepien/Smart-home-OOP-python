import unittest
from smart_home.domain import InteligentnyDom, Lampa, Termostat, CzujnikRuchu, StatusUrzadzenia


class TestLampa(unittest.TestCase):

    def test_domyslny_status(self):
        lampa = Lampa("L001", "Lampa", "Salon")
        self.assertEqual(lampa.status, StatusUrzadzenia.WYLACZONE)

    def test_id_urzadzenia(self):
        lampa = Lampa("L001", "Lampa", "Salon")
        self.assertEqual(lampa.idUrzadzenia, "L001")

    def test_pobierz_status(self):
        lampa = Lampa("L001", "Lampa", "Salon")
        self.assertEqual(lampa.pobierzStatus(), StatusUrzadzenia.WYLACZONE)

    def test_zmien_status(self):
        lampa = Lampa("L001", "Lampa", "Salon")
        lampa.zmienStatus(StatusUrzadzenia.WLACZONE)
        self.assertEqual(lampa.status, StatusUrzadzenia.WLACZONE)

    def test_wlacz(self):
        lampa = Lampa("L001", "Lampa", "Salon")
        lampa.wlacz()
        self.assertEqual(lampa.status, StatusUrzadzenia.WLACZONE)

    def test_wylacz(self):
        lampa = Lampa("L001", "Lampa", "Salon")
        lampa.wlacz()
        lampa.wylacz()
        self.assertEqual(lampa.status, StatusUrzadzenia.WYLACZONE)

    def test_ustaw_poziom(self):
        lampa = Lampa("L001", "Lampa", "Salon")
        lampa.ustawPoziom(80.0)
        self.assertEqual(lampa.jasnosc, 80.0)


class TestTermostat(unittest.TestCase):

    def test_domyslna_temperatura(self):
        termostat = Termostat("T001", "Termostat", "Korytarz")
        self.assertEqual(termostat.temperatura, 20.0)

    def test_wlacz(self):
        termostat = Termostat("T001", "Termostat", "Korytarz")
        termostat.wlacz()
        self.assertEqual(termostat.status, StatusUrzadzenia.WLACZONE)

    def test_ustaw_poziom(self):
        termostat = Termostat("T001", "Termostat", "Korytarz")
        termostat.ustawPoziom(22.5)
        self.assertEqual(termostat.temperatura, 22.5)


class TestCzujnikRuchu(unittest.TestCase):

    def test_domyslny_wykryto_ruch(self):
        czujnik = CzujnikRuchu("C001", "Czujnik", "Przedpokój")
        self.assertFalse(czujnik.wykrytoRuch)

    def test_wlacz(self):
        czujnik = CzujnikRuchu("C001", "Czujnik", "Przedpokój")
        czujnik.wlacz()
        self.assertEqual(czujnik.status, StatusUrzadzenia.WLACZONE)

    def test_wylacz(self):
        czujnik = CzujnikRuchu("C001", "Czujnik", "Przedpokój")
        czujnik.wlacz()
        czujnik.wylacz()
        self.assertEqual(czujnik.status, StatusUrzadzenia.WYLACZONE)


class TestInteligentnyDom(unittest.TestCase):

    def test_nazwa_domu(self):
        dom = InteligentnyDom("Mój Dom")
        self.assertEqual(dom.nazwaDomu, "Mój Dom")

    def test_dodaj_urzadzenie(self):
        dom = InteligentnyDom("Dom")
        lampa = Lampa("L001", "Lampa", "Salon")
        dom.dodajUrzadzenie(lampa)
        self.assertEqual(len(dom.urzadzenia), 1)

    def test_usun_urzadzenie(self):
        dom = InteligentnyDom("Dom")
        lampa = Lampa("L001", "Lampa", "Salon")
        dom.dodajUrzadzenie(lampa)
        dom.usunUrzadzenie(lampa)
        self.assertEqual(len(dom.urzadzenia), 0)

    def test_znajdz_urzadzenie(self):
        dom = InteligentnyDom("Dom")
        lampa = Lampa("L001", "Lampa", "Salon")
        dom.dodajUrzadzenie(lampa)
        self.assertEqual(dom.znajdzUrzadzenie("L001"), lampa)

    def test_wlacz_wszystkie_przelaczalne(self):
        dom = InteligentnyDom("Dom")
        dom.dodajUrzadzenie(Lampa("L001", "Lampa", "Salon"))
        dom.dodajUrzadzenie(Termostat("T001", "Termostat", "Korytarz"))
        dom.wlaczWszystkiePrzelaczalne()
        for urzadzenie in dom.urzadzenia:
            self.assertEqual(urzadzenie.status, StatusUrzadzenia.WLACZONE)

    def test_zarzadzaj_wlacz(self):
        dom = InteligentnyDom("Dom")
        lampa = Lampa("L001", "Lampa", "Salon")
        dom.dodajUrzadzenie(lampa)
        dom.zarzadzajUrzadzeniem(lampa, "wlacz")
        self.assertEqual(lampa.status, StatusUrzadzenia.WLACZONE)

    def test_zarzadzaj_wylacz(self):
        dom = InteligentnyDom("Dom")
        lampa = Lampa("L001", "Lampa", "Salon")
        dom.dodajUrzadzenie(lampa)
        dom.zarzadzajUrzadzeniem(lampa, "wlacz")
        dom.zarzadzajUrzadzeniem(lampa, "wylacz")
        self.assertEqual(lampa.status, StatusUrzadzenia.WYLACZONE)


if __name__ == "__main__":
    unittest.main()
