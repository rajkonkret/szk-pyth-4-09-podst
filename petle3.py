# petla while
# sterowana warunkiem

licznik = 0
while True:
    print("komunikat!!!")  # pętla nieskończona
    licznik += 1
    if licznik > 10:
        break  # przerwij bieżacy blok

print(licznik)
licznik = 0
while licznik < 10:
    print("Komunikat!!!!!!")
    licznik += 1

lista = []
lista2 = []
while True:
    wej = input("Podaj liczbę")  # str
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)  # ['6', '7', '8', '43', '24']
print(lista2)

# ['3', '4', '5', '67']  # str
# [3, 4, 5, 67]  # int
