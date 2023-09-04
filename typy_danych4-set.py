# set , zbiór - przechowuje nizduplikowane elementy
# tracimy kolejność przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
print(lista)
print(type(lista))  # <class 'list'>

zbior = set(lista)  # tworzenie seta z listy
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}
print(type(zbior))  # <class 'set'>

pusta_lista = []
zb2 = set()  # tworzenie pustego zbioru
print(zb2)  # set()
zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}

zbior.remove(55)  # usuniecie elemntu ze zbioru
print(zbior)  # {
# , 66, 777, 11, 44, 18, 22}

print(zbior.pop())
print(zbior)  # {66, 777, 11, 44, 18, 22}
zbior.pop()
print(zbior)  # {777, 11, 44, 18, 22}

lista2 = list(zbior)  # tworzenie listy ze zbioru
print(lista2)  # [777, 11, 44, 18, 22]

zbior2 = {66, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {66, 18, 52, 999, 11, 44, 62}

print(zbior | zbior2)  # suma zbiorów {66, 999, 777, 11, 44, 18, 52, 22, 62}
print(zbior & zbior2)  # częśc wspólna {18, 11, 44}
print(zbior - zbior2)  # różnica  {777, 22}

print(zbior.difference(zbior2))  # {777, 22}
print(zbior2.difference(zbior))  # {66, 52, 62, 999}

first, second, third = "ABC"
print(first, second, third)  # A B C

_, value, _ = [1, 2, 3]
print(value)  # 2 odrzuciliśmy pierwszy i ostatni element

