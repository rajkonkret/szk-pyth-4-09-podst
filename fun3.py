a = 10
b = 10


def dodaj():
    a = 6  # lokalne zmienne w zakresie tej funkcji
    b = 7  # nie wpływaja na zmiane wartosci zmiennych o tej samej nazwie w wyzszym zakresie
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # oznacza użycie wewnątrz funkcji zmiennej globalnej
    a = 6
    b = 7
    print(a + b)


print("Zmienna a z góry", a)
dodaj()  # 13
print("Zmienna a z góry", a)  # Zmienna a z góry 10
dodaj2()  # 20
print("Zmienna a z góry", a)  # Zmienna a z góry 10
dodaj3()  # 13
print("Zmienna a z góry", a)  # Zmienna a z góry 6
dodaj2()  # 16 a nie 20
