from abc import ABC, abstractmethod
from enum import Enum
from typing import Protocol, runtime_checkable


class StatusUrzadzenia(Enum):
    WLACZONE = "wlaczone"
    WYLACZONE = "wylaczone"


class Urzadzenie(ABC):
    def __init__(self, idUrzadzenia: str, nazwaPrzyjazna: str, lokalizacja: str):
        self.__idUrzadzenia = idUrzadzenia
        self.__nazwaPrzyjazna = nazwaPrzyjazna
        self.__lokalizacja = lokalizacja
        self.__status = StatusUrzadzenia.WYLACZONE

    @property
    def idUrzadzenia(self) -> str:
        return self.__idUrzadzenia

    @property
    def nazwaPrzyjazna(self) -> str:
        return self.__nazwaPrzyjazna

    @property
    def lokalizacja(self) -> str:
        return self.__lokalizacja

    @property
    def status(self) -> StatusUrzadzenia:
        return self.__status

    @status.setter
    def status(self, wartosc: StatusUrzadzenia) -> None:
        self.__status = wartosc

    def pobierzStatus(self) -> StatusUrzadzenia:
        return self.status

    def zmienStatus(self, wartosc: StatusUrzadzenia) -> None:
        self.status = wartosc

    @abstractmethod
    def pobierzSzczegolowyOpis(self) -> str:
        pass


class InteligentnyDom:
    def __init__(self, nazwaDomu: str = "Inteligentny Dom"):
        self.__nazwaDomu = nazwaDomu
        self.__urzadzenia: list = []

    @property
    def nazwaDomu(self) -> str:
        return self.__nazwaDomu

    @property
    def urzadzenia(self) -> list:
        return self.__urzadzenia

    def dodajUrzadzenie(self, urzadzenie: Urzadzenie) -> None:
        self.__urzadzenia.append(urzadzenie)

    def usunUrzadzenie(self, urzadzenie: Urzadzenie) -> None:
        self.__urzadzenia.remove(urzadzenie)

    def znajdzUrzadzenie(self, id_lub_nazwa: str) -> Urzadzenie | None:
        for u in self.__urzadzenia:
            if u.idUrzadzenia == id_lub_nazwa or u.nazwaPrzyjazna == id_lub_nazwa:
                return u
        return None

    def wyswietlStatusWszystkichUrzadzen(self) -> None:
        for urzadzenie in self.__urzadzenia:
            print(urzadzenie.pobierzSzczegolowyOpis())

    def wlaczWszystkiePrzelaczalne(self) -> None:
        for urzadzenie in self.__urzadzenia:
            if isinstance(urzadzenie, IPrzelaczalne):
                urzadzenie.wlacz()

    def zarzadzajUrzadzeniem(self, urzadzenie: Urzadzenie, akcja: str, wartosc: float = None) -> None:
        if akcja == "wlacz" and isinstance(urzadzenie, IPrzelaczalne):
            urzadzenie.wlacz()
        elif akcja == "wylacz" and isinstance(urzadzenie, IPrzelaczalne):
            urzadzenie.wylacz()
        elif akcja == "ustawPoziom" and isinstance(urzadzenie, IRegulowane) and wartosc is not None:
            urzadzenie.ustawPoziom(wartosc)


@runtime_checkable
class IPrzelaczalne(Protocol):
    def wlacz(self) -> None:
        ...

    def wylacz(self) -> None:
        ...


@runtime_checkable
class IRegulowane(Protocol):
    def ustawPoziom(self, poziom: float) -> None:
        ...


class Lampa(Urzadzenie, IPrzelaczalne, IRegulowane):
    def __init__(self, idUrzadzenia: str, nazwaPrzyjazna: str, lokalizacja: str):
        super().__init__(idUrzadzenia, nazwaPrzyjazna, lokalizacja)
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
        return f"Lampa '{self.nazwaPrzyjazna}' [{self.lokalizacja}] - status: {self.status.value}, jasność: {self.__jasnosc}%"


class Termostat(Urzadzenie, IPrzelaczalne, IRegulowane):
    def __init__(self, idUrzadzenia: str, nazwaPrzyjazna: str, lokalizacja: str):
        super().__init__(idUrzadzenia, nazwaPrzyjazna, lokalizacja)
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
        return f"Termostat '{self.nazwaPrzyjazna}' [{self.lokalizacja}] - status: {self.status.value}, temperatura: {self.__temperatura} st. C"


class CzujnikRuchu(Urzadzenie, IPrzelaczalne):
    def __init__(self, idUrzadzenia: str, nazwaPrzyjazna: str, lokalizacja: str):
        super().__init__(idUrzadzenia, nazwaPrzyjazna, lokalizacja)
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
        return f"Czujnik ruchu '{self.nazwaPrzyjazna}' [{self.lokalizacja}] - status: {self.status.value}, ruch: {'wykryto' if self.__wykrytoRuch else 'brak'}"
