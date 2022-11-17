from src.dictable import csv_to_list_of_dicts, get_headers_from_csv

experimental_list_of_dicts = [
    {
        "name": "Janusz",
        "last_name": "Skotarczak"
    },
    {
        "name": "John",
        "last_name": "Doe",
        "age": 11
    }
]

#dt = Dictable(experimental_list_of_dicts)

dt = csv_to_list_of_dicts('example.csv', delimiter=';')

print(get_headers_from_csv('example.csv', delimiter=';'))

print(dt.dictable)
print(dt.headers)
print(dt.rows)
print(dt.table)
