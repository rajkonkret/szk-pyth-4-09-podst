wiek = 47
rok = 2023
temp = 36.6
wiek2 = 45.5  # float

print(temp)
print(type(temp))  # <class 'float'> - zmiennoprzecinkowy

print(5 * wiek)
print(5 * "wiek")  # wiekwiekwiekwiekwiek

print(wiek + rok)
print(wiek * rok)
print(wiek - rok)
print(wiek / rok)  # 0.023232822540781017
print(wiek // rok)  # część całkowita z dzielenia u nas 0
print(wiek ** rok)  # potęgowanie
print(wiek % rok)  # modulo, czyli reszta z dzielenia
print(5 % 2)  # reszta 1 bo 2 * 2 = 4, 5 - 4 = 1 - wynik modulo

print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print(0.2 + 0.8)  # 1.0 - float
print(0.2 + 0.7)  # 0.8999999999999999
# we float występuje bład zaokrąglenia
# float jest przechowywany w postaci mantysty i wykładnika 0.9 x 2 ^12
print(0.2 + 0.3)
# 13:30


# typ logiczny
# prawda lub fałsz
# True, False
czy_znasz_pythona = True
print(czy_znasz_pythona)
print(type(czy_znasz_pythona))  # <class 'bool'>
print(int(czy_znasz_pythona))  # True - 1  , int() - rzutowanie na int
czy_znasz_pythona = False
print(int(czy_znasz_pythona))  # 0

x = 1
print(bool(x))  # bool() - rzutowanie na typ logiczny, True

x = 100
print(bool(x))  # True

x = -10
print(bool(x))  # True

x = 0
print(bool(x))  # False

x = 'radek'
print(bool(x))  # True

x = None
print(bool(x))  # False

x = ''
print(bool(x))  # False
# wszystko inne niz 0, None, pusty zbiór, pusta kolekcja będzie True

# działąnia logiczne

print(True and True)  # True
print(True and False)  # False
print(False and True)  # False
print(False and False)  # False

print(True or True)  # True
print(False or False)  # False
print(False or True)  # True
print(True or False)  # True

print(not False)  # True
print(not True)  # False

x = 0
print(not x == 1)  # True
