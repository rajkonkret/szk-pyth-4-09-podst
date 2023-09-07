class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)
# shift + tab - cofnięcie wciecia

try:
    raise MyException("Wystąpił wyjątek")  # rise - rzucenie wyjątku
except MyException:
    print("Wystąpił wyjątek MyException")  # Wystąpił wyjątek MyException
except Exception as e:
    print("Bład", e)
print("Program nadal działa")
