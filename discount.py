from datetime import date, timedelta, datetime

today = date.today()
print(today)  # 2023-09-05
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2023-09-05 13:45:42.617098
#
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2023-09-06

print(time.hour)
print(today.day)

formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 05/09/2023

formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 13:50

products = [
    {'sku': 1, 'exp_date': today, 'price': 100.0},
    {'sku': 2, 'exp_date': tomorrow, 'price': 50.0},
    {'sku': 3, 'exp_date': today, 'price': 80},
    {'sku': 4, 'exp_date': today, 'price': 180},
    {'sku': 5, 'exp_date': today, 'price': 280},
    {'sku': 6, 'exp_date': tomorrow, 'price': 450},
    {'sku': 7, 'exp_date': today, 'price': 90},
]

print(products)

for product in products:
    if product['exp_date'] != today:
        continue  # wraca na poczatek petli, do następnej iteracji pętli bez wykonywania dalszych instrukcji programu
    product['price'] *= 0.8  # price = price * 0.8
    print(f"""
    Price for sku = {product['sku']}
    is now {product['price']}""")
