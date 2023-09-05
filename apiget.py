import requests as re

url = 'http://api.nbp.pl/api/exchangerates/rates/A/USD/'
response = re.get(url)
print(response)
# <Response [200]>
# 200 - ok
# 3... posrednie błedy
# 4.. grube błedy - 404 - brak zasobu, 400 bad request
# http
# get - pobranie danych  read
# post - zapisanie danychdo zasobu - create
# put - to jest update
# delete - delete
# CRUD
table = response.json()
print(table)
# {'table': 'A', 'currency': 'euro', 'code': 'EUR',
#  'rates': [{'no': '171/A/NBP/2023', 'effectiveDate': '2023-09-05', 'mid': 4.4764}]}
# wypisac z odpowiedzi z serwera code,mid
print(table['code'])  # EUR
print(table['rates'])  # [{'no': '171/A/NBP/2023', 'effectiveDate': '2023-09-05', 'mid': 4.4764}]
print(table['rates'][0])  # {'no': '171/A/NBP/2023', 'effectiveDate': '2023-09-05', 'mid': 4.4764}
print(table['rates'][0]['mid'])  # 4.4764
print(table['rates'][0]['effectiveDate'])  # 2023-09-05

url = 'http://api.nbp.pl/api/cenyzlota'
re2 = re.get(url)
table2 = re2.json()  # [{'data': '2023-09-05', 'cena': 257.55}]
print(table2[0]['cena'])  # 257.55
