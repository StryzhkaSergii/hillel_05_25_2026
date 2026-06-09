# tuple - immutable, iterable

my_names = ("Alex", "Den", "Viktor")
print(id(my_names))
print(type(my_names))
print(my_names[0])

my_names = my_names + ("Ivan" , "Sofa")
print(my_names)
print(id(my_names))

for name in my_names:
    print(name)

print(my_names[1:])