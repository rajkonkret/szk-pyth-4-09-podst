# sqlite3 - baza sql w jednym pliku - baza relacyjna
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza danych została podłaczona")
except sqlite3.Error as e:
    print("Bład ppodczas podlacania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")
       