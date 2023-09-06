import csv

filename = 'records.csv'

fields = []
rows = []

with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))  # wyszukujemy automatycznie jaki delimiter jest w pliku csv
    print(dialect.quotechar)
    print(dialect.delimiter)  # ;
    csv_f.seek(0)  # powrot na początek pliku
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter.__str__())

    fields = next(csvreader)  # next() - odczytuje bieżącą linię(0), ustawia wskaźnik na następną
    for row in csvreader:  # wczytanie poszczególnych wierszy
        rows.append(row)

    print("Suma wierszy", csvreader.line_num)  # Suma wierszy 5

print(fields)  # ['name', 'branch', 'year', 'cgpa']
print(rows)
# [['Tomek', 'COE', '2', '9.1'], ['Radek', 'COS', '4', '9'],
# ['Zenek', 'COT', '3', '9.2'], ['radek', 'coe', '3', '9']]
print(rows[2][0])  # Zenek