import pandas as pd

# pip install pandas

data = pd.read_csv('records.csv', delimiter=";")
print(data)
#     name branch  year  cgpa
# 0  Tomek    COE     2   9.1
# 1  Radek    COS     4   9.0
# 2  Zenek    COT     3   9.2
# 3  radek    coe     3   9.0

print(data.columns)  # Index(['name', 'branch', 'year', 'cgpa'], dtype='object')
print(data.values)
# [['Tomek' 'COE' 2 9.1]
#  ['Radek' 'COS' 4 9.0]
#  ['Zenek' 'COT' 3 9.2]
#  ['radek' 'coe' 3 9.0]]
print(data.values[0])  # ['Tomek' 'COE' 2 9.1]
print(data.items)
# <bound method DataFrame.items of     name branch  year  cgpa
# 0  Tomek    COE     2   9.1
# 1  Radek    COS     4   9.0
# 2  Zenek    COT     3   9.2
# 3  radek    coe     3   9.0>
