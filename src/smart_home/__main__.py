from smart_home.domain import InteligentnyDom, Lampa, Termostat, CzujnikRuchu
from smart_home.gui import AplikacjaDom

if __name__ == "__main__":
    dom = InteligentnyDom("Mój Inteligentny Dom")
    dom.dodajUrzadzenie(Lampa("L001", "Lampa sufitowa", "Salon"))
    dom.dodajUrzadzenie(Termostat("T001", "Termostat główny", "Korytarz"))
    dom.dodajUrzadzenie(CzujnikRuchu("C001", "Czujnik wejście", "Przedpokój"))

    print(f"\n=== {dom.nazwaDomu} ===")

    print("\nStatus wszystkich urządzeń:")
    dom.wyswietlStatusWszystkichUrzadzen()

    print("\nWłączanie urządzeń przez zarzadzajUrzadzeniem:")
    for u in dom.urzadzenia:
        dom.zarzadzajUrzadzeniem(u, "wlacz")
    dom.wyswietlStatusWszystkichUrzadzen()

    print("\nSzukanie urządzenia 'L001':")
    znaleziony = dom.znajdzUrzadzenie("L001")
    if znaleziony:
        dom.zarzadzajUrzadzeniem(znaleziony, "ustawPoziom", 75.0)
        print(znaleziony.pobierzSzczegolowyOpis())

    print("\nWyłączanie wszystkich przez zarzadzajUrzadzeniem:")
    for u in dom.urzadzenia:
        dom.zarzadzajUrzadzeniem(u, "wylacz")
    dom.wyswietlStatusWszystkichUrzadzen()

    print("\nUruchamianie GUI...")
    app = AplikacjaDom(dom)
    app.mainloop()
