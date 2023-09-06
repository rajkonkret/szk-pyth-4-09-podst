# pliki csv
# pliki rozdzielone znakiem podziału
# Radek,Maciek,Zenek

import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '9']

dict_x = [
    {'branch': 'COE', 'cgpa': 9.1, 'year': 2, 'name': 'Tomek'},
    {'branch': 'COS', 'cgpa': 9, 'year': 4, 'name': 'Radek'},
    {'branch': 'COT', 'cgpa': 9.2, 'year': 3, 'name': 'Zenek'},
]

dict2 = dict(zip(fields, row))
print(dict2)  # {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '9'}

filename = 'records.csv'

with open(filename, 'w', newline='') as csv_f:
    # csvwriter = csv.writer(csv_f)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    # csvwriter.writerow(row)  - zapis pojedynczego wiersza
    csvwriter.writeheader()  # zapisuje nazwy kolumn
    csvwriter.writerows(dict_x)  # zapisuje wiersze z naszego słownika
    csvwriter.writerow(dict2)
