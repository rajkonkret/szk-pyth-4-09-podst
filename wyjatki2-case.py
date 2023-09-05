while True:
    try:
        z = input("Podaj działąnie + - * /")
        a = int(input("Podaj pierwszą liczbę"))
        b = int(input("Podaj drugą liczbę"))

        match z:
            case "+":
                print(f"Wynik działąnia {a} + {b} = {a + b}")
            case "-":
                print(f"Wynik działania {a} - {b} = {a - b}")
            case "*":
                print(f"Wynik działania {a} * {b} = {a * b}")
            case "/":
                print(f"Wynik działania {a} / {b} = {a / b}")
            case _:
                break
    except ZeroDivisionError:
        print("Nie dziel przez zero")
    except ValueError:
        print("bład wartości")
    else:
        print("Nie ma błedu")
    finally:
        print("Zawsze")
