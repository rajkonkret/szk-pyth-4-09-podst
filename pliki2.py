import chardet

# pip install chardet
file_path = 'test.log'
with open(file_path, 'rb') as file:
    raw_date = file.read()

result = chardet.detect(raw_date)
print(result)  # {'encoding': 'utf-8', 'confidence': 0.99, 'language': ''}
encoding = result['encoding']

# próbka musi być dość duza
print(raw_date.decode(encoding=encoding))