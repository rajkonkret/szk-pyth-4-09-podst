class Car:
    """
    Klasa samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        # tabnine
        self.__predkosc = 0  # pole prywatne

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def hamuj(self):
        self.__predkosc -= 10

    def licznik(self):
        print(f"Jedziesz z prędkością {self.__predkosc} km/h")

    def __zmien_bieg(self):  # funkcja prywatna
        print("Zmiana biegu")


car1 = Car("Bmw", 2004)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# print(car1.__predkosc)
car1.__predkosc = 100  # tak nie robimy
car1.licznik()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
print(car1.__predkosc)
car1.licznik()
