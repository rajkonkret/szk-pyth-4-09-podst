import pickle  # wspomaga operowanie danymi złożonymi

lista = [1, 2, 3, 4, 5]
with open('test_lista.txt', 'w') as f:
    f.write(str(lista))  # rzutowanie na str

with open('test_lista.txt', 'r') as f:
    lines = f.read()

print(lines)  # [1, 2, 3, 4, 5]
print(type(lines))  # <class 'str'>
print(lines[0])  # [

# wb - zapis bajtowy, zapisuje wszystkie bajty tak jak wyglądaja w pamięci
with open("lista_pickle.log", 'wb') as file:
    pickle.dump(lista, file)

with open('lista_pickle.log', 'rb') as file:
    loaded_list = pickle.load(file)

print(loaded_list)  # [1, 2, 3, 4, 5]
print(type(loaded_list))  # <class 'list'>
print(loaded_list[0])  # 1

data = {"name": "John", 'age': 30, 'city': "New York"}
with open('dictionary_pickle.log', 'wb') as f:
    pickle.dump(data, f)

with open('dictionary_pickle.log', 'rb') as f:
    data_loaded = pickle.load(f)

print(data_loaded)
print(type(data_loaded))  # <class 'dict'>
print(data_loaded['name'])  # John

with open('data_pickle.log', 'wb') as f:
    pickle.dump(lista, f)
    pickle.dump(data, f)

with open('data_pickle.log', 'rb') as f:
    loaded_l = pickle.load(f)
    loaded_d = pickle.load(f)

print(loaded_l)
print(loaded_d)
# [1, 2, 3, 4, 5]
# {'name': 'John', 'age': 30, 'city': 'New York'}

serialized_data = pickle.dumps(data)
print(serialized_data)
# b'\x80\x04\x95-\x00\x00\x00\x00\x00\x00\x00}\x94
# (\x8c\x04name\x94\x8c\x04John\x94\x8c\x03age\x94K\x1e\x8c\x04city\x94\x8c\x08New York\x94u.'

deserialized_data = pickle.loads(serialized_data)
print(deserialized_data)  # {'name': 'John', 'age': 30, 'city': 'New York'}
print(type(serialized_data))
print(type(deserialized_data))
# <class 'bytes'>
# <class 'dict'>