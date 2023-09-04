# krotka (tupla) - niezmienialna lista
# zienna niezmienna
tupla = 'radek'
print(type(tupla))  # <class 'str'>

tupla2 = ("Tomek", "Radek", "Zenek", "Marek")
print(type(tupla2))  # <class 'tuple'>

tpl2 = ("radek",)
print(type(tpl2))  # <class 'tuple'>
# tupla wypełnia znamiona zmiennej
tupla3 = 43, 55, 22.34, 11, 200
print(type(tupla3))
print(tupla3)  # (43, 55, 22.34, 11, 200)

temp = 37, 5
print(type(temp))  # <class 'tuple'>

print(tupla2.count("Tomek"))  # 1
print(tupla2.index("Tomek"))  # 0

a, b = 1, 2
print(a)
print(b)

a, b = 1, (2, 3)
print(a)
print(b)

a, *b = 1, 2, 3
print(a)  # 1
print(b)  # [2, 3]
print(type(b))  # <class 'list'>
# rozpakowanie tupli

# ("Tomek", "Radek", "Zenek", "Marek")
imie1, *imie2, imie3 = tupla2
print(imie1)
print(imie2)
print(imie3)
# Tomek
# ['Radek', 'Zenek']
# Marek

# 15:35

lista = list(tupla3)  # zamiana tupli na liste
print(lista)  # [43, 55, 22.34, 11, 200]
print(type(lista))  # <class 'list'>
