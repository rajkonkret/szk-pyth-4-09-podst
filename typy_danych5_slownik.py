# słownik - para klucz watość {"name":"Radek"}
# {"klucz" : "wartośc"}

dict = {}  # pusty słownik
print(dict)  # {}
print(type(dict))  # <class 'dict'>

dict['imie'] = "Radek"
print(dict)  # {'imie': 'Radek'}

dict['wiek'] = 39
print(dict)  # {'imie': 'Radek', 'wiek': 39}

print(dict.keys())  # wypisanie kluczy
print(dict.values())  # wypisanie wartości
print(dict.items())  # wypisanie par
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 39])
# dict_items([('imie', 'Radek'), ('wiek', 39)])

dict.update({'data': '12-12-2023'})
print(dict)  # {'imie': 'Radek', 'wiek': 39, 'data': '12-12-2023'}

dictionary = {'x': '2'}
dictionary.update([('y', 3), ('z', 0)])
print(dictionary)  # {'x': '2', 'y': 3, 'z': 0}

# stworzyc słownik, dwie pary klucz wartosc, polskie:angielski
dict2 = {'imie': 'name', 'kot': 'cat'}
print(dict2['imie'])  # name
# wypisanie kluczy ze słownika
# pobranie słowa do przetłumaczenia od użytkownika
# wypisanie przetłuamczonego słowa

print("Mamy w słowniku", dict2.keys())  # Mamy w słowniku dict_keys(['imie', 'kot'])
key = input("Podaj słówko do przetłumaczenia")
# input() - pobiera znaki z klawiatury, zwraca str()
print(dict2[key.replace(" ", "").lower()])  # wypisujemy ze słownika wartość dla klucza znajdującego sie w zmiennej key

a = int(input("Podaj pierwszą liczbę"))
b = int(input("Podaj drugą liczbę"))
# print(int(a) + int(b))
print(a + b)
# dodaałem