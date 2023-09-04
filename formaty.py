user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float, zmiennoprzecinkowy
liczba = 134567456234  # int

print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %s masz teraz %d lat" % (wiek, user))  # TypeError: %d format: a real number is required, not str
# %s - łańcuch znaków (string)
# %r - reprezentacja obiektu (repr)
# %d - liczba całkowita (integer)
# %i - liczba całkowita (integer)
# %o - liczba w formacie ósemkowym (octal)
# %u - liczba całkowita bez znaku (unsigned decimal)
# %x - liczba w formacie szesnastkowym (hexadecimal)
# %X - liczba w formacie szesnastkowym (hexadecimal) z wielkimi literami
# %e - liczba w notacji naukowej (exponential)
# %E - liczba w notacji naukowej (exponential) z wielkimi literami
# %f - liczba zmiennoprzecinkowa (float)
# %F - liczba zmiennoprzecinkowa (float)
# %g - liczba zmiennoprzecinkowa (float) w formacie kompaktowym
# %G - liczba zmiennoprzecinkowa (float) w formacie kompaktowym z wielkimi literami
# %c - pojedynczy znak (character)
# %p - adres pamięci obiektu
# %% - znak % (percent)

print('Witaj %(user)s, masz teraz %(age)d lat' % {'user': user, "age": wiek})  # Witaj Tomek, masz teraz 39 lat

print("witaj {} masz teraz {} lat".format(user, wiek))  # witaj Tomek masz teraz 39 lat
print("witaj {} masz teraz {} lat".format(wiek, user))  # witaj 39 masz teraz Tomek lat

print(f"Witaj {user}, masz teraz {wiek} lat")  # f - fstring, formatowanie tekstu
# Witaj Tomek, masz teraz 39 lat

print("Używamy wersji Pythona %i" % 3)  # Używamy wersji Pythona 3
print("Używamy wersji Pythona %f" % 3.9)  # Używamy wersji Pythona 3.900000
print("Używamy wersji Pythona %.1f" % 3.9)  # Używamy wersji Pythona 3.9
print("Używamy wersji Pythona %.2f" % 3.9)  # Używamy wersji Pythona 3.90
print("Używamy wersji Pythona %.0f" % 3.9)  # Używamy wersji Pythona 4
print("Używamy wersji Pythona %.f" % 3.9)  # Używamy wersji Pythona 4
# zero miejsc po przecinku. pamietac, że zaokrągla
x = 3.14
print("Zero miejsc po przecinku %.f" % x)  # Zero miejsc po przecinku 3
print("Oryginalny x=", x)  # Oryginalny x= 3.14

print(f"Używamy wersji Pythona {wersja}")  # Używamy wersji Pythona 3.900001
print(f"Używamy wersji Pythona {wersja:.1f}")  # Używamy wersji Pythona 3.9
print(f"Używamy wersji Pythona {wersja:.2f}")  # Używamy wersji Pythona 3.90
print(f"Używamy wersji Pythona {wersja:.0f}")  # Używamy wersji Pythona 4

print(f"{user:>10}")  # "     Tomek" - dopełnił spacjami do długosci 10, wyrównał do prawej
print(f"{user:>20}")  # "               Tomek"
print(f"{user:<10}")  # "Tomek     " - wyrównał do lewej, długośc wyrównał do 10
print(f"{user:^10}")  # "  Tomek   " - tekst wyśrodkowany

print(liczba)  # 134567456234
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 134,567,456,234
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 134.567.456.234
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 134 567 456 234
print(f"Nasza duża liczba {liczba:,}")  # Nasza duża liczba 134,567,456,234
print(f"Nasza duża liczba {liczba:,}".replace(",", "."))  # Nasza duża liczba 134.567.456.234

a = 8
b = 7

print(f"Porównanie {a} > {b}", a > b)  # Porównanie 8 > 7 True
print(f"Porównanie {a} < {b}", a < b)  # Porównanie 8 < 7 False
print(f"Porównanie {a} == {b}", a == b)  # Porównanie 8 == 7 False - == - znak porównania a == b zwraca True lub False
print(f"Porównanie {a} != {b}", a != b)  # Porównanie 8 != 7 True
print(f"Porównanie {a} >= {b}", a >= b)  # PPorównanie 8 >= 7 True
print(f"Porównanie {a} <= {b}", a <= b)  # Porównanie 8 <= 7 False
