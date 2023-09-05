# match case

lista = []
lang = input('Podaj znany ci język programowania')

match lang.lower().replace(" ", ""):
    case 'python':
        lista.append(lang)
    case 'java':
        lista.append(lang)
    case _:  # odpowiednik else, default
        print("Nie znam takiego języka")
print(lista)
