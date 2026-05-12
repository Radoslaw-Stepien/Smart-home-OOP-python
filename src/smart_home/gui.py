import customtkinter as ctk
from smart_home.domain import InteligentnyDom, Lampa, Termostat, CzujnikRuchu, StatusUrzadzenia

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


def interpoluj_kolor(wartosc, min_val, max_val, kolor_min, kolor_max):
    t = max(0.0, min(1.0, (wartosc - min_val) / (max_val - min_val)))
    r1, g1, b1 = int(kolor_min[1:3], 16), int(kolor_min[3:5], 16), int(kolor_min[5:7], 16)
    r2, g2, b2 = int(kolor_max[1:3], 16), int(kolor_max[3:5], 16), int(kolor_max[5:7], 16)
    r = int(r1 + (r2 - r1) * t)
    g = int(g1 + (g2 - g1) * t)
    b = int(b1 + (b2 - b1) * t)
    return f"#{r:02x}{g:02x}{b:02x}"

class KafelekLampa(ctk.CTkFrame):
    def __init__(self, parent, lampa: Lampa):
        super().__init__(parent, corner_radius=15, fg_color="#1e1e2e")
        self.lampa = lampa

        ctk.CTkLabel(self, text="💡 " + lampa.nazwaPrzyjazna, font=ctk.CTkFont(size=16, weight="bold")).pack(padx=15, pady=(15, 2))
        ctk.CTkLabel(self, text=lampa.lokalizacja, text_color="gray").pack(padx=15)

        self.przelacznik = ctk.CTkSwitch(self, text="", command=self._przelacz)
        self.przelacznik.pack(pady=10)

        ctk.CTkLabel(self, text="Jasność").pack()
        self.suwak = ctk.CTkSlider(self, from_=0, to=100, command=self._zmien_jasnosc)
        self.suwak.set(0)
        self.suwak.pack(padx=15, fill="x")

        self.etykieta_jasnosc = ctk.CTkLabel(self, text="0%")
        self.etykieta_jasnosc.pack()
        self.wskaznik = ctk.CTkLabel(self, text="", height=30, fg_color="#2a2a2a", corner_radius=8)
        self.wskaznik.pack(padx=15, fill="x", pady=(5, 0))

        self.etykieta_status = ctk.CTkLabel(self, text="⬤ wyłączone", text_color="#ff6b6b")
        self.etykieta_status.pack(pady=(5, 15))

    def _przelacz(self):
        if self.przelacznik.get():
            self.lampa.wlacz()
            self.etykieta_status.configure(text="⬤ włączone", text_color="#69db7c")
        else:
            self.lampa.wylacz()
            self.etykieta_status.configure(text="⬤ wyłączone", text_color="#ff6b6b")

    def _zmien_jasnosc(self, wartosc):
        self.lampa.ustawPoziom(round(wartosc))
        self.etykieta_jasnosc.configure(text=f"{round(wartosc)}%")
        kolor = interpoluj_kolor(wartosc, 0, 100, "#2a2a2a", "#ffff66")
        self.wskaznik.configure(fg_color=kolor)


class KafelekTermostat(ctk.CTkFrame):
    def __init__(self, parent, termostat: Termostat):
        super().__init__(parent, corner_radius=15, fg_color="#1e1e2e")
        self.termostat = termostat

        ctk.CTkLabel(self, text="🌡️ " + termostat.nazwaPrzyjazna, font=ctk.CTkFont(size=16, weight="bold")).pack(padx=15, pady=(15,2))
        ctk.CTkLabel(self, text=termostat.lokalizacja, text_color="gray").pack(padx=15)

        self.przelacznik = ctk.CTkSwitch(self, text="", command=self._przelacz)
        self.przelacznik.pack(pady=10)

        ctk.CTkLabel(self, text="Temperatura").pack()
        self.suwak = ctk.CTkSlider(self, from_=15, to=30, command=self._zmien_temperature)
        self.suwak.set(20)
        self.suwak.pack(padx=15, fill="x")
        self.etykieta_temp = ctk.CTkLabel(self, text="20.0 st. C")
        self.etykieta_temp.pack()
        self.wskaznik = ctk.CTkLabel(self, text="", height=30, fg_color="#4fc3f7", corner_radius=8)
        self.wskaznik.pack(padx=15, fill="x", pady=(5, 0))

        self.etykieta_status = ctk.CTkLabel(self, text="⬤ wyłączone", text_color="#ff6b6b")
        self.etykieta_status.pack(pady=(5,15))

    def _przelacz(self):
        if self.przelacznik.get():
            self.termostat.wlacz()
            self.etykieta_status.configure(text="⬤ włączone", text_color="#69db7c")
        else:
            self.termostat.wylacz()
            self.etykieta_status.configure(text="⬤ wyłączone", text_color="#ff6b6b")
    
    def _zmien_temperature(self, wartosc):
        self.termostat.ustawPoziom(round(wartosc, 1))
        self.etykieta_temp.configure(text=f"{round(wartosc, 1)} st. C")
        kolor = interpoluj_kolor(wartosc, 15, 30, "#4fc3f7", "#ff5722")
        self.wskaznik.configure(fg_color=kolor)


class KafelekCzujnik(ctk.CTkFrame):
    def __init__(self, parent, czujnik: CzujnikRuchu):
        super().__init__(parent, corner_radius=15, fg_color="#1e1e2e")
        self.czujnik = czujnik

        ctk.CTkLabel(self, text="🚶 " + czujnik.nazwaPrzyjazna, font=ctk.CTkFont(size=16, weight="bold")).pack(padx=15, pady=(15, 2))
        ctk.CTkLabel(self, text=czujnik.lokalizacja, text_color="gray").pack(padx=15)

        self.przelacznik = ctk.CTkSwitch(self, text="", command=self._przelacz)
        self.przelacznik.pack(pady=10)

        self.etykieta_ruch = ctk.CTkLabel(self, text="Brak ruchu", text_color="gray")
        self.etykieta_ruch.pack()

        ctk.CTkButton(self, text="Symuluj ruch", command=self._symuluj_ruch).pack(pady=10)

        self.etykieta_status = ctk.CTkLabel(self, text="⬤ wyłączone", text_color="#ff6b6b")
        self.etykieta_status.pack(pady=(5, 15))

    def _przelacz(self):
        if self.przelacznik.get():
            self.czujnik.wlacz()
            self.etykieta_status.configure(text="⬤ włączone", text_color="#69db7c")
        else:
            self.czujnik.wylacz()
            self.etykieta_status.configure(text="⬤ wyłączone", text_color="#ff6b6b")

    def _symuluj_ruch(self):
        if self.czujnik.status == StatusUrzadzenia.WLACZONE:
            self.czujnik.wykrytoRuch = True
            self.etykieta_ruch.configure(text="🚨 Wykryto ruch!", text_color="#ffd43b")
            self.after(3000, self._reset_ruch)

    def _reset_ruch(self):
        self.czujnik.wykrytoRuch = False
        self.etykieta_ruch.configure(text="Brak ruchu", text_color="gray")


class AplikacjaDom(ctk.CTk):
    def __init__(self, dom: InteligentnyDom):
        super().__init__()
        self.dom = dom
        self.title("Inteligentny Dom")
        self.geometry("900x500")
        self.resizable(False, False)

        ctk.CTkLabel(self, text="🏠 Inteligentny Dom", font=ctk.CTkFont(size=24, weight="bold")).pack(pady=20)

        siatka = ctk.CTkFrame(self, fg_color="transparent")
        siatka.pack(padx=20, pady=10, fill="both", expand=True)

        for i, urzadzenie in enumerate(dom.urzadzenia):
            if isinstance(urzadzenie, Lampa):
                kafelek = KafelekLampa(siatka, urzadzenie)
            elif isinstance(urzadzenie, Termostat):
                kafelek = KafelekTermostat(siatka, urzadzenie)
            elif isinstance(urzadzenie, CzujnikRuchu):
                kafelek = KafelekCzujnik(siatka, urzadzenie)
            kafelek.grid(row=i // 3, column=i % 3, padx=10, pady=10, sticky="nsew")

        for col in range(3):
            siatka.columnconfigure(col, weight=1)
