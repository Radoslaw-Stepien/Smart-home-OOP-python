from smart_home.domain import InteligentnyDom, Lampa, Termostat, CzujnikRuchu
from smart_home.gui import AplikacjaDom

if __name__ == "__main__":
    dom = InteligentnyDom()
    dom.dodajUrzadzenie(Lampa("Lampa sufitowa", "Salon"))
    dom.dodajUrzadzenie(Termostat("Termostat główny", "Korytarz"))
    dom.dodajUrzadzenie(CzujnikRuchu("Czujnik wejście", "Przedpokój"))


    app = AplikacjaDom(dom)
    app.mainloop()
