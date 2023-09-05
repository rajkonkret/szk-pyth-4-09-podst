# json - {"name":"Radek"}
# obiekt typu klucz wartośc
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(person_dict)  # {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', "w") as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {"name": "Radek", "age": 40, "czy_pali": null}
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }

# {
#     "age": 40,
#     "czy_pali": null,
#     "name": "Radek"
# }

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}

print(type(data))  # <class 'dict'>
print(data['name'])  # Radek
