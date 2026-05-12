# Smart Home OOP Python

Projekt zaliczeniowy z programowania obiektowego w Pythonie. System zarządzania urządzeniami w inteligentnym domu — pokazuje hierarchię klas, interfejsy, enkapsulację i polimorfizm.

## Instalacja

Wymagany Python 3.12+ — tkinter jest wbudowany w standardowy instalator Pythona dla Windows.

Utwórz i aktywuj środowisko wirtualne:

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

Zainstaluj zależności projektu (jedyna zewnętrzna biblioteka to `customtkinter` — nowoczesny wygląd interfejsu GUI oparty na tkinter):

```bash
pip install -r requirements.txt
```

## Jak uruchomić

Aplikacja (GUI):

```bash
PYTHONPATH=src python -m smart_home
```

Testy:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

## Struktura repo

```text
smart-home-oop-python/
├── src/smart_home/
│   ├── domain.py       # wszystkie klasy domenowe
│   ├── gui.py          # interfejs graficzny (customtkinter)
│   ├── __init__.py     # publiczny interfejs pakietu
│   └── __main__.py     # entry point
├── tests/
│   └── test_smart_home.py
├── docs/
│   └── uml/
│       └── diagram.md  # diagram klas (Mermaid)
└── examples/
```

## Diagram klas

```mermaid
classDiagram
    class StatusUrzadzenia {
        <<enumeration>>
        WLACZONE
        WYLACZONE
    }

    class Urzadzenie {
        <<abstract>>
        -__nazwa : str
        -__lokalizacja : str
        -__status : StatusUrzadzenia
        +nazwa() str
        +lokalizacja() str
        +status() StatusUrzadzenia
        +pobierzSzczegolowyOpis()* str
    }

    class InteligentnyDom {
        -__urzadzenia : list
        +urzadzenia() list
        +dodajUrzadzenie(urzadzenie)
        +wyswietlStatusWszystkichUrzadzen()
        +wlaczWszystkiePrzelaczalne()
    }

    class IPrzelaczalne {
        <<interface>>
        +wlacz()
        +wylacz()
    }

    class IRegulowane {
        <<interface>>
        +ustawPoziom(poziom float)
    }

    class Lampa {
        -__jasnosc : float
        +jasnosc() float
        +wlacz()
        +wylacz()
        +ustawPoziom(poziom float)
        +pobierzSzczegolowyOpis() str
    }

    class Termostat {
        -__temperatura : float
        +temperatura() float
        +wlacz()
        +wylacz()
        +ustawPoziom(poziom float)
        +pobierzSzczegolowyOpis() str
    }

    class CzujnikRuchu {
        -__wykrytoRuch : bool
        +wykrytoRuch() bool
        +wlacz()
        +wylacz()
        +pobierzSzczegolowyOpis() str
    }

    Urzadzenie <|-- Lampa
    Urzadzenie <|-- Termostat
    Urzadzenie <|-- CzujnikRuchu
    IPrzelaczalne <|.. Lampa
    IPrzelaczalne <|.. Termostat
    IPrzelaczalne <|.. CzujnikRuchu
    IRegulowane <|.. Lampa
    IRegulowane <|.. Termostat
    InteligentnyDom "1" o-- "0..*" Urzadzenie
    Urzadzenie --> StatusUrzadzenia
```

## Testy jednostkowe

Uruchamianie:

```bash
PYTHONPATH=src python -m unittest discover -s tests -v
```

| Klasa testowa         | Metoda testowa                    | Co weryfikuje                                          | Wynik |
| --------------------- | --------------------------------- | ------------------------------------------------------ | :---: |
| `TestLampa`           | `test_domyslny_status`            | Nowa lampa ma status `WYLACZONE`                       |  ✓   |
| `TestLampa`           | `test_wlacz`                      | Po `wlacz()` status zmienia się na `WLACZONE`          |  ✓   |
| `TestLampa`           | `test_wylacz`                     | Po `wylacz()` status wraca do `WYLACZONE`              |  ✓   |
| `TestLampa`           | `test_ustaw_poziom`               | `ustawPoziom(80.0)` ustawia jasność na 80.0            |  ✓   |
| `TestTermostat`       | `test_domyslna_temperatura`       | Nowy termostat ma domyślną temperaturę 20.0°C          |  ✓   |
| `TestTermostat`       | `test_wlacz`                      | Po `wlacz()` status zmienia się na `WLACZONE`          |  ✓   |
| `TestTermostat`       | `test_ustaw_poziom`               | `ustawPoziom(22.5)` ustawia temperaturę na 22.5°C      |  ✓   |
| `TestCzujnikRuchu`    | `test_domyslny_wykryto_ruch`      | Nowy czujnik ma `wykrytoRuch = False`                  |  ✓   |
| `TestCzujnikRuchu`    | `test_wlacz`                      | Po `wlacz()` status zmienia się na `WLACZONE`          |  ✓   |
| `TestCzujnikRuchu`    | `test_wylacz`                     | Po `wylacz()` status wraca do `WYLACZONE`              |  ✓   |
| `TestInteligentnyDom` | `test_dodaj_urzedzenie`           | `dodajUrzadzenie()` zwiększa listę urządzeń o 1        |  ✓   |
| `TestInteligentnyDom` | `test_wlacz_wszystkie_przylaczalne` | `wlaczWszystkiePrzelaczalne()` włącza wszystkie urządzenia |  ✓   |
| **Łącznie**           |                                   | **12 testów — wszystkie zaliczone (0 błędów)**         | **✓** |

## Model domenowy

| Klasa / Interfejs  | Rola                                                               |
| ------------------ | ------------------------------------------------------------------ |
| `Urzadzenie`       | Abstrakcyjna klasa bazowa. Enkapsuluje nazwę, lokalizację, status. |
| `Lampa`            | Urządzenie przełączalne i regulowane (poziom jasności).            |
| `Termostat`        | Urządzenie przełączalne i regulowane (temperatura docelowa).       |
| `CzujnikRuchu`     | Urządzenie wykrywające ruch.                                       |
| `StatusUrzadzenia` | Enum: `WLACZONE` / `WYLACZONE`.                                    |
| `IPrzelaczalne`    | Interfejs (Protocol): `wlacz()`, `wylacz()`.                       |
| `IRegulowane`     | Interfejs (Protocol): `ustawPoziom()`.                             |
| `InteligentnyDom`  | Agreguje urządzenia. Zarządza nimi i demonstruje polimorfizm.      |

## Pokryte tematy OOP

- dziedziczenie i `super()` — `Lampa`, `Termostat`, `CzujnikRuchu` po `Urzadzenie`
- enkapsulacja — prywatne pola urządzeń
- abstrakcyjna klasa bazowa (ABC) — `Urzadzenie` wymusza implementację `pobierzSzczegolowyOpis()`
- polimorfizm — `wyswietlStatusWszystkichUrzadzen()` wywołuje `pobierzSzczegolowyOpis()` na każdym urządzeniu
- interfejsy (Protocol) — `IPrzelaczalne`, `IRegulowane`
- Enum — `StatusUrzadzenia`
- kolekcja `list` — lista urządzeń w `InteligentnyDom`
