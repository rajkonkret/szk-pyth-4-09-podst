# funkcja, która oblicza średnią

def liczby(i=0, *cyfry):
    print(cyfry)  # (1, 2, 3, 4, 5), (2, 3, 4, 5)
    suma = 0
    try:
        for c in cyfry:
            suma += c
        print(suma)
        count = len(cyfry)
        avg = suma / count
    except ZeroDivisionError:
        print("Uczeń nie ma ocen")
    except Exception as e:
        print("Błąd", e)
    else:
        print(f"Średnia dla ucznia {i} wynosi {avg}")


liczby()
liczby(1, 2, 3, 4, 5)
liczby(1, 2, 3, 4, 5, 4, 6, 7, 8, 9)
liczby("1", 2, 3, 4, 5, 4, 6, 7, 8, 9)
a = 1, 2, 3
i, *cyfry = a
print(i)
print(cyfry)
# dodac oddzielną obsługę błedu dzielenia przez 0
