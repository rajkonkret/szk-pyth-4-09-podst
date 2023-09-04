print()  # wyswietlanie na ekranie tekstu
# znaczek komentarza
# PEP8
# ctrl alt l - automatyczne formatownie linii

print("Nazywam się Radek")
# ctrl d - kopiowanie lini
print('Nazywam się Radek')
# Nazywam się Radek
# Nazywam się Radek
# ctrl / (?) - automatyczny komentarz
# 11:30

# type() - wypisanie typu danych
print(type("Radek"))  # <class 'str'> - typ tekstowy

print(39)
print(type(39))  # <class 'int'> - liczby całkowite (int)

print("14" + "39")  # 1439 - konkatenacja - łaczenie stringów
# print(39 + "14") - błąd TypeError: unsupported operand type(s) for +: 'int' and 'str'
# Traceback (most recent call last):
#   File "/Users/radoslawjaniak/PycharmProjects/szk-pyth-4-09-pods/pierwszy.py", line 21, in <module>
#     print(39 + "14")
#           ~~~^~~~~~
# TypeError: unsupported operand type(s) for +: 'int' and 'str'
print(39 + 14)  # 53 - prwidłowe dodawanie

print(5 * "4")  # 44444 - powielanie tekstu
print(5 * "*")

# zmienna - pudełko na dane
imie = "Radek"
print(imie)
print(type(imie))  # <class 'str'> - tekst
print("Radek \'tytuł\'")  # \ - znak ucieczki
print("Radek 'tytuł'")

imie = 48
print(imie)
print(type(imie))  # <class 'int'>

imie: str = 56  # dodana podpowiedź, nie waliduje typu
print(imie)  # 56
print(type(imie))  # <class 'int'>
imie: str = "Radek"
print(imie)
print(type(imie))  # <class 'str'>

wiek = 48
print(wiek)
print(type(wiek))  # <class 'int'>
print(imie + str(wiek))  # str() - rzutowanie na string(tekstowy)
#  + dla stringów oznacza konkatenację, czyli łaczenie stringów

wiek = "Radek"
print(type(wiek))
