# funkcje zwracające wynik

def dodaj(a, b):  # dwa obowiązkowe argumenty
    return a + b  # odesłąnie wyniku do miejsca gdzie funkcja zostałą wywołana


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 4))  # 9
print(dodaj(5, 6) + dodaj(6, 7))  # 24
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))  # 1070.0
print(oblicz_vat(vat=15, cena=5000))  # 5750.0

zm = oblicz_vat(1000)
print(zm)  # 1230.0
print(type(zm))  # <class 'float'>

if zm == 1230:
    print("Prawidłowo")
