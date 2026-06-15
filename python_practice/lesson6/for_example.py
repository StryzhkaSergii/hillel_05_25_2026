# for number in range(10):
#     print(number)

names = ["Alex", "Den", "Ivan"]
ages = [10,20,30]
# name = "Alex"
# print(name)
# for name in names:
#     print(name)

# name = names[0]
# print(name)
# name = names[1]
# print(name)
# name = names[2]
# print(name)

# for name in names:
#     print(name)
#     for age in ages:
#         print(age)

for _ in range(10):
    print("Hello")

response = [
    {"id": 1, "name":"Read only", "description": "For all users"},
    {"id": 2, "name":"RW", "description": "For write and read"},
    {"id": 3, "name":"all", "description": "For admin"},
    {"id": 3, "name":"all", "description": "For admin"},
    {"id": None, "name":"broken", "description": None}
]

for permission in response:
    if permission.get("id") is None:
        print(f"Alarm no id for permission {permission}")

uniq_ids = []
for perm in response:
    if perm.get("id") in uniq_ids:
        print(f"Id's are not uniq, id = {perm.get('id')}")
        break
    else:
        uniq_ids.append(perm.get('id'))

# break - закінчує цикл при досягнені break
# continue - переходить на наступну ітерацію
# if element in list: True
# if 3 in [1,2,3] -> True

names = ["Alex", "Den", "Ivan"]
for name in names:
    if name is "Den":
        continue
    print(f"You are not Den so I will work with you: {name}")

for k in range(10):
    print(k)
    if k == 5:
        break
else:
    print("We can see this message")

# спрацьовує якщо не спрацював break