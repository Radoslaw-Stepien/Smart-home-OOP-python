from abc import ABC, abstractmethod
from enum import Enum
from typing import Protocol


class StatusUrzadzenia(Enum):
    WLACZONE = "wlaczone"
    WYLACZONE = "wylaczone"


class Urzadzenie(ABC):
    def __init__(self, nazwa: str, lokalizacja: str):
        self.nazwa = nazwa
        self.lokalizacja = lokalizacja
        self.status = StatusUrzadzenia.WYLACZONE

    @abstractmethod
    def pobierzSzczegolowyOpis(self) -> str:
        pass


class InteligentnyDom:
    def __init__(self):
        self.urzadzenia: list = []

    def dodajUrzadzenie(self, urzadzenie: Urzadzenie):
        self.urzadzenia.append(urzadzenie)


class IPrzelaczalne(Protocol):
    def wlacz(self) -> None:
        ...

    def wylacz(self) -> None:
        ...


class IRegulowalne(Protocol):
    def ustawPoziom(self, poziom: float) -> None:
        ...


class Lampa(Urzadzenie, IPrzelaczalne, IRegulowalne):
    def __init__(self, nazwa: str, lokalizacja: str):
        super().__init__(nazwa, lokalizacja)
        self.jasnosc: float = 0.0

    def wlacz(self) -> None:
        self.status = StatusUrzadzenia.WLACZONE

    def wylacz(self) -> None:
        self.status = StatusUrzadzenia.WYLACZONE

    def ustawPoziom(self, poziom: float) -> None:
        self.jasnosc = poziom

    def pobierzSzczegolowyOpis(self) -> str:
        return f"Lampa '{self.nazwa}' [{self.lokalizacja}] - status: {self.status.value}, jasność: {self.jasnosc}%"


class Termostat(Urzadzenie, IPrzelaczalne, IRegulowalne):
