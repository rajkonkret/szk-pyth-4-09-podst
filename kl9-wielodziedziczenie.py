# wielodziedziczenie
# w Pythonie kalsa może dziedziczyć po wielu klasach

class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("Metoda z klasa B")


class C(B, A):  # dziedziczenie po klasach A i B - kolejność ma znaczenie
    """
    Klasa C, dziedziczyłą po klaach A i B
    """

    def method(self):
        print("Metoda z klasy C")  # Metoda z klasy C nadpisanie
        super().method()  # Metoda z kalsy A użycie metody z klasy nadrzędnej czyli A
        B.method(self)


a = A()
a.method()  # Metoda z kalsy A

b = B()
b.method()  # Metoda z klasa B

c = C()
c.method()  #
print(C.__mro__)
# (A, B)
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
# (B, A)
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
