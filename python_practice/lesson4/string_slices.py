my_name = "Alex is my name"

print(my_name[0])

# slices

print(my_name[:4])
print(my_name[5:])
print(my_name[0:4])
print(my_name[::2])
print(my_name[1::2])

part_of_name = my_name[:4]
print(part_of_name)
print(id(my_name))
print(id(part_of_name))