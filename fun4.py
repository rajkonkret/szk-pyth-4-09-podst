# funkcja zagnieżdżona
def fun1():
    print("To jest fun1")

    def fun2():  # funcja zagnieżdzona
        print("To jest fun2")

    return fun2  # bez nawiasów, zwroci adres pamieci do funkcji


# fun1()  # uzycie funkcji, nazwa funkcji i nawiasy ()
xFun = fun1()
print(xFun)  # <function fun1.<locals>.fun2 at 0x100531a80>
print(type(xFun))  # <class 'function'>
xFun()  # To jest fun2
