class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Menedzer(Pracownik):
    """
    Menedzer
    """

    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 7500)
pracownik.przedstaw_sie()  # Cześć, jestem Jan Kowalski
wyn_prac = pracownik.oblicz_pensje()
print(f"Wynagrodzenie dla pracownika {pracownik.imie} {pracownik.nazwisko}: {wyn_prac}")
# Wynagrodzenie dla pracownika Jan Kowalski: 7500

menago = Menedzer("Anna", "Nowak", 8500, 2000)
menago.przedstaw_sie()  # Cześć, jestem Anna Nowak
wyn_menago = menago.oblicz_pensje()
print(f"Wynagrodzenie dla menedżera {menago.imie} {menago.nazwisko}: {wyn_menago}")
# Cześć, jestem Jan Kowalski
# Wynagrodzenie dla pracownika Jan Kowalski: 7500
# Cześć, jestem Anna Nowak
# Wynagrodzenie dla menedżera Anna Nowak: 10500
