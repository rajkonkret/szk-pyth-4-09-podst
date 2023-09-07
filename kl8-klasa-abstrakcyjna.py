# klasa abstrakcyjna - taka klasa z której nie można stworzyć obiektu
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "lecę z szybkościa", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Orzel(Ptak):
    def poluj(self):
        print("Tu", self.gatunek, "Ropoczynam polowanie")

    def wydaj_odglos(self):
        print("piiiiiiii")


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def wydaj_odglos(self):
        print("kokokokokokoko")

    def dziobanie(self):
        print("Tu", self.gatunek, "Idę sobie podziobać")


# po oznaczeniu metody @abstractmethod
# orzel = Ptak("orzel", 20)  # TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos
# orzel.latam()  # Tu orzel lecę z szybkościa 20
#
# kura = Ptak("kura", 0)
# kura.latam()  # Tu kura lecę z szybkościa 0
# nie moząna stworzyc obiektu  klasy w której jest metoda oznaczona jako abstrakcyjna
or2 = Orzel('orzel', 15)
or2.latam()
or2.wydaj_odglos()
or2.poluj()

kura2 = Kura("kura")
kura2.latam()
kura2.wydaj_odglos()
kura2.dziobanie()
# 11:20
