tekst = "Witaj świecie"
print(tekst)  # Witaj świecie

print(tekst.upper())  # zamienia na duże litery  """ Return a copy of the string converted to uppercase. """
tekst2 = tekst.upper()
print(tekst)
print(tekst2)  # WITAJ ŚWIECIE
# teksty są niemutowalne

print(tekst.lower())  # witaj świecie - małe litery

print(tekst)  # Witaj świecie

print(tekst.removeprefix("Witaj"))  # " świecie"
print(tekst.removesuffix("świecie"))  # "Witaj "
print(tekst)  # Witaj świecie

encoded_s = tekst.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
# b - ciąg binarny
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))  # Witaj świecie

# liczba wystąpień literki "i"
print(tekst.count("i"))  # 3
# numeracja zaczyna sie od 0
print(tekst.count("i", 0, 4))  # 1, zbiór niedomkniety
print(tekst.count("j", 0, 4))  # 0, zbiór niedomkniety, znaku na indeksie 4 nie sprawdza
# indeksowanie znaków
# Witaj
# 01234

print(len(tekst))  # len() - długośc kolekcji 13

imie = "Radek"
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona \b"
print(tekst_format)
# Mam na imię Radek
#  # i lubię Pythona
# \n - Nowa linia
# \r - Powrót karetki
# \t - Tabulacja pozioma
# \b - Powrót kursora (usuwa poprzedni znak)
# \f - Przesunięcie strony
# \v - Tabulacja pionowa
# ' - Apostrof (literał apostrofu)
# " - Cudzysłów (literał cudzysłowu)
# \a - Dźwięk systemowy lub sygnał alarmowy
# \ooo - Znak o wartości oktalnej (np. \012 reprezentuje znak nowej linii)
# \xhh - Znak o wartości szesnastkowej (np. \x0A reprezentuje znak nowej linii)
# \uXXXX - Znak Unicode o wartości czteroznakowego kodu szesnastkowego
# \UXXXXXXXX - Znak Unicode o wartości ośmioznakowego kodu szesnastkowego
# \N{name} - Znak Unicode o podanej nazwie
euro_sign = "\u20AC"
print(euro_sign)  # €

starszy = "Witaj %s"
# %s - wstaw string
print(type(imie))
print(starszy % imie)  # Witaj Radek

print("""
Tekst
 wielolinijkowy""")
# Tekst
#  wielolinijkowy

print("""

""")
print("Witaj {} {}".format(imie, "pp"))  # Witaj Radek pp
# pod klamerki podstawi wartość zmiennej imie
