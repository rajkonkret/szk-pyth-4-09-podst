def odejmij(a, b):
    return a - b


print(odejmij(6, 7))  # -1
# lambda - uproszczona wersja funkcji
odejmij2 = lambda a, b: a - b
print(odejmij2(6, 7))  # -1

oblic_vat = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblic_vat(1000))
print(oblic_vat(1000, 7))

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(8))
print(wiek(15))
print(wiek(18))
print(wiek(26))

lista = [1, 2, 3, 4, 5, 6, 8, 10, 23, 50]
l = []

for i in lista:
    l.append(i * 2)

print(l)  # [2, 4, 6, 8, 10, 12, 16, 20, 46, 100]


def zmien(x):
    return x * 2


# map() - mapowanie kolekcji, czyli zamiana wszystkich elemntów w kolekcji wg zaadanego schematu
print(f"Zastosowanie map: {list(map(zmien, lista))}")
# Zastosowanie map: [2, 4, 6, 8, 10, 12, 16, 20, 46, 100]
print(f"Zastosowanie map: {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map: [2, 4, 6, 8, 10, 12, 16, 20, 46, 100]

# filte() - sprawdza warunek i zwraca tylko spełniajace warunek
print(f"Zastosowanie filter: {list(filter(lambda x: x < 3, lista))}")  # Zastosowanie filter: [1, 2]
# zrobic filter zwracjący większe od 8
# zrobic filter zwracajćy większe od 3 mniejsze od 20
print(f"Zastosowanie filter: {list(filter(lambda x: x > 8, lista))}")  # Zastosowanie filter: [10, 23, 50]
print(f"Zastosowanie filter: {list(filter(lambda x: 3 < x < 20, lista))}")  # Zastosowanie filter: [4, 5, 6, 8, 10]
# x > 3 and x < 20 -?> 3 < x < 20
