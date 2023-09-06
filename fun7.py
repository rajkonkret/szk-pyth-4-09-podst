def connect(**opcje):  # parametry słownikowe
    print(opcje)
    print(type(opcje))
    connect_param = {
        'host': '127.0.0.7',
        'port': '8080'
    }
    print(connect_param)
    print(type(connect_param))
    connect_param['pwd'] = opcje
    print(connect_param)
    connect_param.update({'pwd2': opcje})
    print(connect_param)


def connect2(*opcje):  # ({'name': 'Radek'},)
    print(opcje)


connect()  # {} {"name":"Radek}, klucz=wartosc
# connect(1)  # TypeError: connect() takes 0 positional arguments but 1 was given
#
# connect(1, 2, 3)
# connect(klucz='wartość')  # {'klucz': 'wartość'}
# connect2({'name': 'Radek'})  # ({'name': 'Radek'},)
connect(root="/")  # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'root': '/'}}
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'root': '/'}, 'pwd2': {'root': '/'}}
connect(root="/", port="9090", name="Radek", klucz='wartosc')
# {'host': '127.0.0.7', 'port': '8080', 'pwd': {'root': '/', 'port': '9090', 'name': 'Radek', 'klucz': 'wartosc'},
#  'pwd2': {'root': '/', 'port': '9090', 'name': 'Radek', 'klucz': 'wartosc'}}
connect(a=8)  # {'host': '127.0.0.7', 'port': '8080', 'pwd': {'a': 8}, 'pwd2': {'a': 8}}
