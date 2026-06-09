my_name, den_name, vik_name = ("Alex", "Den", "Viktor")
my_names = ("Alex", "Den", "Viktor")

print(den_name)
print(my_names)
print(*my_names)

# error
#my_name, not_my_name = ("Alex", "Den", "Viktor")

my_name, *not_my_name, vik_name = ("Alex", "Den", "Viktor", "Sofa", "Ivan")
print(my_name)
print(not_my_name)
print(vik_name)

some_text = "placeholder"

tuple_text = tuple(some_text)
print(tuple_text)

print(list(my_names))

tuple_with_one_el = (42,)
not_tuple = (42)
print(type(tuple_with_one_el))
print(type(not_tuple))