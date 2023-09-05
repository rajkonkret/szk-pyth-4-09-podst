import random

# random - generowanie liczb pseudolosowych

print(random.randint(1, 6))  # int 1..6
print(random.random())  # float 0..0.999999
print(random.random() * 6)  # float 0..5.999999
print(random.randrange(6))  # int 0..5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))

lista2 = list(range(1, 50))  # 1..50
print(lista2)

# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))
# print(random.choice(lista2))

wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
wyn = random.choice(lista2)
print(wyn)
lista2.remove(wyn)
# ctrl / - automatyczny komentarz
print(random.choices(lista2, k=6))  # [27, 1, 27, 19, 34, 2]

