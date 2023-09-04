# lista - kolekcja, przechowująca dowolną ilość danych, mogą być przechowywane rózne typy
# zachowuje kolejność dodawania

lista = []  # pusta lista
print(lista)  # []
print(type(lista))  # <class 'list'>

lista.append("Radek")  # append() - dodawanie do listy
lista.append("Maciek")
lista.append("Jaśko")
lista.append("Zenek")
#                0 lub -4 1 lub -3  2 lub -2 3 lub -1
print(lista)  # ['Radek', 'Maciek', 'Jaśko', 'Zenek']
# indeksy są numerowane od 0
print(lista[0])  # wypisanie elemntu po indeksie, 0 = Radek
print(lista[2])  # Jaśko
# print(lista[10])  # IndexError: list index out of range
print(len(lista))  # len() - długość kolekcji = 4
print(lista[-1])  # Zenek
print(lista[-2])
print(lista[0:3])  # ['Radek', 'Maciek', 'Jaśko'] od indeksu 0 do 2. indeks 3 nie jest zabierany
print(lista[:3])  # ['Radek', 'Maciek', 'Jaśko']
print(lista[2:])  # ['Jaśko', 'Zenek']  - obie wartości przedziału włącznie

# nadpisanie elemntu na tym indeksie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Zenek']

# wstawia element w miejscu o indeksie, dodaje do kolekcji
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Zenek']

# usuniecie pierwszego napotkanego elemntu z listy
# print(lista.remove("Maciek"))  # None
lista.remove("Maciek")
print(lista)  # ['Radek', 'Marcin', 'Mikołaj', 'Zenek']

indeks = lista.index('Zenek')

print(lista.pop(indeks))  # Zenek - zwraca element usunięty
print(lista)  # ['Radek', 'Marcin', 'Mikołaj']

a = 1
b = 3
a = b
print(b)
print(a)
a = 7
a, b = b, a
print(a, b)  # 3 7

lista3 = lista.copy()
lista2 = lista  # kopiowanie referencji czyli adres pamieci
print(lista)
print(lista2)
# ['Radek', 'Marcin', 'Mikołaj']
# ['Radek', 'Marcin', 'Mikołaj']
lista.clear()  # usuniecie wszystkich elemntów z listy
print(lista)  # []
print(lista2)  # []
print(lista3)  # ['Radek', 'Marcin', 'Mikołaj']

# liczby = [54, 999, 34, 22, 12.34, 687, 'A']  # TypeError: '<' not supported between instances of 'str' and 'int'
liczby = [54, 999, 34, 22, 12.34, 687]
print(liczby)  # [54, 999, 34, 22, 12.34, 687]
print(type(liczby))  # <class 'list'>
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

lista_osoby = ['radek', 'ola']
lista_osoby.sort()
print(lista_osoby)  # ['ola', 'radek']

liczby.reverse()
print(liczby)  # [999, 687, 54, 34, 22, 12.34]
liczby[3] = 6666
print(liczby)  # [999, 687, 54, 6666, 22, 12.34]
print(liczby[0:3])
print(liczby[-2])
print(liczby[0:-2])
print(liczby[-3:])
# [999, 687, 54]
# 22
# [999, 687, 54, 6666]
# [6666, 22, 12.34]

liczby.remove(54)
print(liczby)

print(liczby.pop(3))
print(liczby)

print(len(liczby))  # długosc kolekcji

tekst = 'Python'

lista_1 = list(tekst)  # zamiana sekwencji na liste
print(lista_1)  # ['P', 'y', 't', 'h', 'o', 'n']
lista_2 = [tekst]  # tworzenie listy z elementem w zmiennej
print(lista_2)  # ['Python']

krotka = tuple(liczby)  # zamiana listy na krotke(tuple)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (999, 687, 6666, 12.34)
