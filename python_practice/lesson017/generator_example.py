# yield


def get_names():
    return ["Alex", "Den", "Ivan"]


def get_names_gen():
    print("return Alex")
    yield "Alex"
    print("return Den")
    yield "Den"
    print("return Ivan")
    yield "Ivan"

print(get_names())
for name in get_names_gen():
    print(name)

all_kvadrats_list = [k**2 for k in range(10)]
print(all_kvadrats_list)
all_kvadrats_gen = (k**2 for k in range(10))
print(all_kvadrats_gen)
# print(list(all_kvadrats_gen))

for el in all_kvadrats_gen:
    print(el)