from abc import ABC, abstractmethod
from enum import Enum
from typing import Protocol, runtime_checkable


class StatusUrzadzenia(Enum):
    WLACZONE = "wlaczone"
    WYLACZONE = "wylaczone"


class Urzadzenie(ABC):
    def __init__(self, nazwa: str, lokalizacja: str):
        self.__nazwa = nazwa
        self.__lokalizacja = lokalizacja
        self.__status = StatusUrzadzenia.WYLACZONE

    @property
    def nazwa(self) -> str:
        return self.__nazwa

    @property
    def lokalizacja(self) -> str:
        return self.__lokalizacja

    @property
    def status(self) -> StatusUrzadzenia:
        return self.__status

    @status.setter
    def status(self, wartosc: StatusUrzadzenia) -> None:
        self.__status = wartosc

    @abstractmethod
    def pobierzSzczegolowyOpis(self) -> str:
        pass


class InteligentnyDom:
    def __init__(self):
        self.__urzadzenia: list = []

    @property
    def urzadzenia(self) -> list:
        return self.__urzadzenia

    def dodajUrzadzenie(self, urzadzenie: Urzadzenie):
        self.__urzadzenia.append(urzadzenie)

    def wyswietlStatusWszystkichUrzadzen(self) -> None:
        for urzadzenie in self.__urzadzenia:
            print(urzadzenie.pobierzSzczegolowyOpis())

    def wlaczWszystkiePrzelaczalne(self) -> None:
        for urzadzenie in self.__urzadzenia:
            if isinstance(urzadzenie, IPrzelaczalne):
                urzadzenie.wlacz()


@runtime_checkable
class IPrzelaczalne(Protocol):
    def wlacz(self) -> None:
        ...

    def wylacz(self) -> None:
        ...


class IRegulowane(Protocol):
    def ustawPoziom(self, poziom: float) -> None:
        ...


class Lampa(Urzadzenie, IPrzelaczalne, IRegulowane):
    def __init__(self, nazwa: str, lokalizacja: str):
        super().__init__(nazwa, lokalizacja)
        self.__jasnosc: float = 0.0

    @property
    def jasnosc(self) -> float:
        return self.__jasnosc

    def wlacz(self) -> None:
        self.status = StatusUrzadzenia.WLACZONE

    def wylacz(self) -> None:
        self.status = StatusUrzadzenia.WYLACZONE

    def ustawPoziom(self, poziom: float) -> None:
        self.__jasnosc = poziom

    def pobierzSzczegolowyOpis(self) -> str:
        return f"Lampa '{self.nazwa}' [{self.lokalizacja}] - status: {self.status.value}, jasność: {self.__jasnosc}%"


class Termostat(Urzadzenie, IPrzelaczalne, IRegulowane):
    def __init__(self, nazwa: str, lokalizacja: str):
        super().__init__(nazwa, lokalizacja)
        self.__temperatura: float = 20.0

    @property
    def temperatura(self) -> float:
        return self.__temperatura

    def wlacz(self) -> None:
        self.status = StatusUrzadzenia.WLACZONE

    def wylacz(self) -> None:
        self.status = StatusUrzadzenia.WYLACZONE

    def ustawPoziom(self, poziom: float) -> None:
        self.__temperatura = poziom

    def pobierzSzczegolowyOpis(self) -> str:
        return f"Termostat '{self.nazwa}' [{self.lokalizacja}] - status: {self.status.value}, temperatura: {self.__temperatura} st. C"


class CzujnikRuchu(Urzadzenie, IPrzelaczalne):
    def __init__(self, nazwa: str, lokalizacja: str):
        super().__init__(nazwa, lokalizacja)
        self.__wykrytoRuch: bool = False

    @property
    def wykrytoRuch(self) -> bool:
        return self.__wykrytoRuch

    @wykrytoRuch.setter
    def wykrytoRuch(self, wartosc: bool) -> None:
        self.__wykrytoRuch = wartosc

    def wlacz(self) -> None:
        self.status = StatusUrzadzenia.WLACZONE

    def wylacz(self) -> None:
        self.status = StatusUrzadzenia.WYLACZONE

    def pobierzSzczegolowyOpis(self) -> str:
        return f"Czujnik ruchu '{self.nazwa}' [{self.lokalizacja}] - status: {self.status.value}, ruch: {'wykryto' if self.__wykrytoRuch else 'brak'}"
