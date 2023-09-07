# dziedziczenie

class Pojazd:
    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor: {self.kolor}")


class Samochod(Pojazd):  # dziedziczenie po klasie Pojazd
    """
    Samochod
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        """
        metoda info dla klasy Samochód
        :return: opisuje pojazd
        """
        super().info()  # wywołanie metody info()  z klasy wyższej
        print(f"Marka: {self.marka}")


poj = Pojazd("Zielony")
poj.info()
car1 = Samochod("Czerwony", "Audi")
car1.info()  # Kolor: Czerwony
# Kolor: Zielony
# Kolor: Czerwony
# Marka: Audi
# bez super().info()
# Kolor: Zielony
# Marka: Audi
print(Samochod.info.__doc__)
# metoda info dla klasy Samochód
# :return: opisuje pojazd