from smart_home.domain import InteligentnyDom, Lampa, Termostat, CzujnikRuchu

if __name__ == "__main__":
    dom = InteligentnyDom()

    lampa = Lampa("Lampa sufitowa", "Salon")
    termostat = Termostat("Termostat główny", "Korytarz")
    czujnik = CzujnikRuchu("Czujnik wejście", "Przedpokój")

    dom.dodajUrzadzenie(lampa)
    dom.dodajUrzadzenie(termostat)
    dom.dodajUrzadzenie(czujnik)

    print("=== Status przed włączeniem ===")
    dom.wyswietlStatusWszystkichUrzadzen()

    dom.wlaczWszystkiePrzelaczalne()
    lampa.ustawPoziom(75.0)
    termostat.ustawPoziom(22.5)

    print("\n=== Status po włączeniu ===")
    dom.wyswietlStatusWszystkichUrzadzen()
