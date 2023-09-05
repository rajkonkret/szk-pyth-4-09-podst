dictionary = {'imie': 'Radek', 'nazwisko': 'kowalski'}

print(type(dictionary))  # <class 'dict'>

# wypisze klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# wypiszemy wartości
for v in dictionary.values():
    print(v)

# wypisze pary
for i in dictionary.items():
    print(i)  # ('nazwisko', 'kowalski')

for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => kowalski

dictionary2 = {'name': 'imie', 'company': 'Comarch'}
print(dictionary2)  # {'name': 'imie', 'company': 'Comarch'}

print(({value: key for key, value in dictionary2.items()}))
# {'imie': 'name', 'Comarch': 'company'}

d2 = {}  # pusty słownik
for key, value in dictionary2.items():
    d2[value] = key

print(d2)  # {'imie': 'name', 'Comarch': 'company'}
# 13:30