# kalkulator
# menu
# pobrac operacje
# wyswietlic wynik
# w pętli while

while True:
    print(f"""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec
    """)
    odp = input("Podaj działąnie jakie chcesz wykonać")  # str
    if odp == '5':
        break
    try:
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą liczbę"))

        if odp == '1':
            print("Dodawanie", a + b)
        elif odp == '2':
            print("Odejmowanie", a - b)
        elif odp == '3':
            print("Mnożenie", a * b)
        elif odp == '4':
            # if b != 0:
            print("Dzielenie", a / b)
            # else:
            #     print("Nie dzielimy przez zero!")
        else:
            print("Nie znam takiej operacji")
    except ValueError:
        print("Bład wartości")

    except ZeroDivisionError:
        print("Nie dziel przez zero!")
    except Exception as e:
        print("Nastąpił bład", e)
    else:  # wykona się gdy nie bedzie błedu
        print("Gdy nie ma błedu")
    finally:  # wykona się zawsze
        print("Zawsze")



