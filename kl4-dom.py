class Dom:
    """
    Klasa opisująca dom w Pythonie
    """

    def __init__(self, metraz, kolor, liczba_okien):
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    def podaj_kolor(self):
        print(f"Mamy kolor {self.__kolor}")

    def podaj_okna(self):
        print(f"Liczba okien {self.__liczba_okien}")

    def podaj_metraz(self):
        print(f"Mamy teraz {self.__metraz} m")

    def zmien_metraz(self):
        wybor = int(input("Podaj nowy metraż"))
        self.__metraz = wybor
        self.podaj_metraz()

    def zmien_kolor(self):
        wybor = input("Podaj nowy kolor")
        self.__kolor = wybor
        self.podaj_kolor()
        self.__farba()

    def zmien_okna(self):
        wybor = int(input("Podaj liczbę okien"))
        self.__liczba_okien = wybor
        self.podaj_okna()

    def __farba(self):
        print(f"Skończyłą sie farba kolor: {self.__kolor}")


dom1 = Dom(500, "biały", 18)
dom1.podaj_okna()
dom1.podaj_kolor()
dom1.podaj_metraz()
dom1.zmien_kolor()
# Podaj nowy kolorpomarańczowy
# Mamy kolor pomarańczowy
# Skończyłą sie farba kolor: pomarańczowy
