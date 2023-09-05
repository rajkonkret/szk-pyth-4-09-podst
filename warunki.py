# warunki - instrukcje sterowania przpływem programu
# if - instrukcja warunkowa

# if warunek:
#   instrukcje do wykonania jeśli warunek jest spełniony

odp = True
if odp:  # jeżeli warunek jest True to wykonuje instrukcje po wcięciu
    print("Brawo")  # wcięcie obowiązkowe
else:
    print('Ucz się dalej')  # w przeciwnym przypadku

print("Dalsza częśc programu")

# podatek = 0.0
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif 35000 < zarobki < 50000:  # zarobki > 35000 and zarobki < 50000
#     podatek = 0.3
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.6
# # po napotkaniu pierwszego warunku True wychodzi do głownej pętli programu po wykonaniu instrukcji z tego bloku
# print(f"Zapłącisz {podatek * zarobki} zł")
# # dodoac prog miedzy 10000 a 29999 podatek 20%

suma_zam = 150
if suma_zam > 100:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabat wynosi {rabacik}")

rabat = 25 if suma_zam > 100 else 0
print(f"Rabat wynosi {rabat}")

lista_bledow = []
alert_system = 'email'
error = 'medium'

error_message = "Stało się coś strasznego"

if alert_system == 'console':  # == porównanie
    print(error_message)
elif alert_system == 'email':
    lista_bledow.append('email')
    # dodjemy waruki jesli bład medium to do listy dodajemy wyraz ostrzezenie, jesli bład krytyczny to do listy
    # wpisujemy critical, jesli błąd inny niz te dwa to do listy wpisujemy inny
    if error == 'medium':
        lista_bledow.append('ostrzeżenie')
    elif error == 'critical':
        lista_bledow.append('krytyczny')
    else:
        lista_bledow.append('inny')
else:
    print("Nieznany")

print(lista_bledow)

# napisac test z historii, geografii, czegokolwiek
# wyswietlic pytanie
# pobrac odpowiedz od użytkownika
# sprawdzic odpowiedz
# wyswietlic wynik

# print()
odp = input("Podaj date Chrztu Polski")  # zwraca str
# if odp == 966 # gdyby odp była liczbą
if odp.lower().replace(" ", "") == "966":
    print("Odpowiedź prawidłowa")
else:
    print("Masz w książce na stronie 23")
