name = "Alex"
print(id(name))

name = name + "Rudyk"
print(id(name))

# mutable types - list, dict, set, bytearray е змінюють адресу в памʼяті при зміні
my_list_names = ["Alex", "Den"]
print(id(my_list_names))
print(my_list_names)

my_list_names.append("Ivan")
print(id(my_list_names))
print(my_list_names)