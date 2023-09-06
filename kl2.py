class Human:
    """
    Klasa opisująca człowieka w Pythonie
    """

    def __init__(self, imie, wiek, plec="k"):  # tzw konstruktor
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        print(f"Mam na imię {self.imie}")

    def podaj_wiek(self):
        print(f"Mam {self.wiek} lat")

    def podaj_plec(self):
        print(f"Jestem {self.plec}")

    def ruszaj(self):
        if self.plec == 'm':
            print("Ruszyłem w drogę")
        else:
            print("Ruszyłam w drogę")


cz1 = Human("Radek", "56", "m")
print(cz1.wiek)
print(cz1.imie)
print(cz1.plec)
cz1.ruszaj()
cz2 = Human("Ania", "34")
print(cz2.plec)
cz2.powitanie()  # Mam na imię Ania
cz2.podaj_plec()  # Jestem k
cz2.ruszaj()