# sqlite3 - baza sql w jednym pliku - baza relacyjna
import sqlite3

# psycopg2 - postgress connect
try:
    sql_connection = sqlite3.connect('sqlite_python.db')

    select = '''
    SELECT * FROM software;
    '''

    update = '''
    UPDATE software SET price = 2000 WHERE id=1;
    '''

    delete = '''
    DELETE FROM software WHERE id=1;
    '''

    cursor = sql_connection.cursor()
    print("Baza danych została podłaczona")

    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 100.0)

    # cursor.execute(update)
    # sql_connection.commit()  # (1, 'Python', 2000.0)

    cursor.execute(delete)
    sql_connection.commit()
except sqlite3.Error as e:
    print("Bład ppodczas podlacania bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych została zamknięta")

# CRUD CREATE, READ, UPDATE, DELETE
# Insert, Select, Update, Delete
# POST, GET, PUT, DELETE
# HEAD - to samo co GET ale pobiera tylko  nagłowek
# 13:35
# 14:15