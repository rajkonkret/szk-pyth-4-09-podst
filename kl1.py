# klasa - szblon opisujący w jakis sposób i jakie cechy ma miec obiekt
# klasa może posiadac pola, funkcje
# instancją klasy jest obiekt

class Human:  # definicja kalsy
    """
    Klasa Human opisująca człowieka w pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        print(f"Nazywam sie {self.imie}")

    def podaj_wiek(self):
        print(f"Mam {self.wiek} lat")


cz1 = Human()  # utworzenie obiektu klasy
print(Human.__doc__)
#     Klasa Human opisująca człowieka w pythonie
print(print.__doc__)
print(cz1)  # <__main__.Human object at 0x104333410>
print(cz1.plec)  # k
cz1.imie = "Radek"
print(cz1.imie)  # Radek
cz1.powitanie()

cz2 = Human()  # stworzenie obiektu
cz2.imie = "Tomek"
cz2.wiek = 67
cz2.plec = "m"
print(cz2.imie)  # v
cz2.powitanie()
cz2.podaj_wiek()  # Mam 67 lat
