import json

# Дані для запису у JSON-файл
user_data = [
    {"name": "John", "age": 30, "city": "New York", "is_active":True},
    {"name": "Alex", "age": 40, "city": "New York", "is_active":False},
    {"name": "Ivan", 'age': 25, "city": "New York", "has_friends":None}
]

user_data_json = json.dumps(user_data)
print(type(user_data_json))
# with open("json_as_str.txt", "w") as f:
#     f.write(user_data_json)

# with open("json_as_str.json", "w") as f:
#     json.dump(user_data, f, indent=4)


with open("json_as_str.txt") as f:
    data = json.loads(f.read())
with open("json_as_str.json") as f:
    data2 = json.load(f)
print(data)
print(data2)