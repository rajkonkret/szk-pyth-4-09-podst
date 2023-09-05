# petle - instrukcje sterowania przepływem programu
# for - pętla iteracyjna
# petla sterowana licznikiem
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i)

for i in range(10):
    pass  # nic nie rób

for _ in range(10):
    pass  # _  niema zmienna

for i in range(10):
    print(i * 2)

lista2 = list(range(1, 50))

for i in range(6):
    wyn = random.choice(lista2)
    lista2.remove(wyn)
    print(wyn)
# hackerrank
# print(lista2)

for i in range(10):
    if i % 2 == 0:
        print(i, "jest parzysta")
# 0 jest parzysta
# 2 jest parzysta
# 4 jest parzysta
# 6 jest parzysta
# 8 jest parzysta

lista3 = [j for j in range(10) if j % 2 == 0]
print(lista3)

lista4 = []
for j in range(10):
    if j % 2 == 0:
        lista4.append(j)

print(lista4)
# [0, 2, 4, 6, 8]
# [0, 2, 4, 6, 8]

for c in lista4:
    if c == 2:
        c += 1  # c = c + 1
    print(c)  # 3
# spam += 1	spam = spam + 1
# spam -= 1	spam = spam - 1
# spam *= 1	spam = spam * 1
# spam /= 1	spam = spam / 1
# spam %= 1	spam = spam % 1

a = 1
a += 1
print(a)
a = 1
a -= 1
print(a)
a = 1
a *= 3
print(a)
a = 1
a %= 2
print(a)
a = 1
a /= 2
print(a)  # 1/2 = 0.5 float

imiona = ['Radek', 'Asia', 'Zbyszek', 'Marcin']
for p in imiona:
    print(p)

# Wypisać imiona z listy i indeks na jakim jest dane imie
# 0 Radek
# 1 Asia
for i in imiona:
    print(imiona.index(i), i)

for i in range(len(imiona)):
    print(i, imiona[i])

# enumerate - zwraca ponumerowaną kolekcję
for p in enumerate(imiona):
    print(p)  # (0, 'Radek')
    a, b = p
    print(a, b)

for p, w in enumerate(imiona):
    print(p, w)

for p, w in enumerate(imiona):
    print(p, w, sep=";", end=" ")
# sep= - znak oddzielający elementy po przecinku(domyślnie spacja)
# end= - znak konca lini (domyślnie enter \n)
print()

ludzie = ['Radek', 'Zenek', 'Asia', 'Marcin', 'Franek']
wiek = [47, 67, 34, 32]

# for p, o in enumerate(ludzie):
#     print(p, o, wiek[p])  # IndexError: list index out of range

# zip()
for k in zip(ludzie, wiek):
    print(k)
# ('Radek', 47)
# ('Zenek', 67)
# ('Asia', 34)
# ('Marcin', 32)

for o, w in zip(ludzie, wiek):
    print(o, w)  # Radek 47

for p in enumerate(zip(ludzie, wiek)):
    print(p)  # (3, ('Marcin', 32))

for i, o in enumerate(zip(ludzie, wiek)):
    print(i, o)  # 3 ('Marcin', 32)

for i, (o, w) in enumerate(zip(ludzie, wiek)):
    print(i, o, w)  # 3 Marcin 32

jezyk = ['java', 'python']

for i, (o, w, j) in enumerate(zip(ludzie, wiek, jezyk)):
    print(i, o, w, j)
# 0 Radek 47 java
# 1 Zenek 67 python

zipped = zip_longest(ludzie, wiek, jezyk, fillvalue='Nan')

# for item in zipped:
#     print(item)
# ('Radek', 47, 'java')
# ('Zenek', 67, 'python')
# ('Asia', 34, 'Nan')
# ('Marcin', 32, 'Nan')
# ('Franek', 'Nan', 'Nan')

for o1, w1, j1 in zipped:
    print(o1, w1, j1)

# Radek 47 java
# Zenek 67 python
# Asia 34 Nan
# Marcin 32 Nan
# Franek Nan Nan

for i in range(0, 10, 2):  # start, stop, krok
    print(i)

for i in range(-10, 0, 2):
    print(i)

for i in range(10, 0, -2):  # pętla w dół
    print(i)
