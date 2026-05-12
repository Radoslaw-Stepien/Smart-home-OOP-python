# Smart Home OOP Python

Projekt zaliczeniowy z programowania obiektowego w Pythonie. System zarządzania urządzeniami w inteligentnym domu — pokazuje hierarchię klas, interfejsy, enkapsulację i polimorfizm.

## Instalacja

Wymagany Python 3.12+.

Na Fedorze/RHEL przed instalacją zależności upewnij się że tkinter jest dostępny:

```bash
sudo dnf install python3-tkinter
```

Na Ubuntu/Debian:

```bash
sudo apt install python3-tk
```

Na Windows tkinter jest wbudowany w standardowy instalator Pythona — nie wymaga dodatkowych kroków.

Następnie zainstaluj zależności projektu:

```bash
pip install -r requirements.txt
```

## Jak uruchomić

Demo:

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
│   ├── __init__.py     # publiczny interfejs pakietu
│   └── __main__.py     # demo / entry point
├── tests/
│   └── test_smart_home.py
├── docs/
│   └── uml/            # diagram klas
└── examples/
```

## Model domenowy

| Klasa / Interfejs  | Rola                                                              |
|--------------------|-------------------------------------------------------------------|
| `Urzadzenie`       | Abstrakcyjna klasa bazowa. Enkapsuluje id, nazwę, lokalizację, status. |
| `Lampa`            | Urządzenie przełączalne i regulowalne (poziom jasności).          |
| `Termostat`        | Urządzenie przełączalne i regulowalne (temperatura docelowa).     |
| `CzujnikRuchu`     | Urządzenie wykrywające ruch.                                      |
| `StatusUrzadzenia` | Enum: `WLACZONE` / `WYLACZONE`.                                   |
| `IPrzelaczalne`    | Interfejs (Protocol): `wlacz()`, `wylacz()`.                      |
| `IRegulowalne`     | Interfejs (Protocol): `ustawPoziom()`.                            |
| `InteligentnyDom`  | Agreguje urządzenia. Zarządza nimi i demonstruje polimorfizm.     |

## Pokryte tematy OOP

- dziedziczenie i `super()` — `Lampa`, `Termostat`, `CzujnikRuchu` po `Urzadzenie`
- enkapsulacja — prywatne pola urządzeń
- abstrakcyjna klasa bazowa (ABC) — `Urzadzenie` wymusza implementację `pobierzSzczegolowyOpis()`
- polimorfizm — `wyswietlStatusWszystkichUrzadzen()` wywołuje `pobierzSzczegolowyOpis()` na każdym urządzeniu
- interfejsy (Protocol) — `IPrzelaczalne`, `IRegulowalne`
- Enum — `StatusUrzadzenia`
- kolekcja `list` — lista urządzeń w `InteligentnyDom`
