# funkcje - wydzielony blok programu, mozliwy do wielokrotnego wywoływania

a = 6
b = 7


def dodaj():  # to jest tylko definicja funkcji, funkcja bezargumentowa
    print(a + b)  # przejeła wartości z wyzszego scopa(zakresu)


def dodaj2(a, b):
    print(a + b)


def odejmij(a, b, c=0):  # c - argument domyślny, nieobowiązkowy
    print(a - b - c)


def odejmij2(liczba1, liczba2):
    print(liczba1 - liczba2)


dodaj()  # wywołanie funkcji: nazwa funkcji i (), 13
dodaj2(4, 5)  # 9
# dodaj2()  # TypeError: dodaj2() missing 2 required positional arguments: 'a' and 'b'
odejmij(1, 2)  # -1
odejmij(1, 2, 3)  # -4
odejmij(b=5, a=8, c=9)  # -6
odejmij(5, 8, 9)  # -12
odejmij2(1, 2)
odejmij2(liczba2=5, liczba1=4)
print(dodaj())  # None
# print(dodaj() + dodaj2(5, 6))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'

