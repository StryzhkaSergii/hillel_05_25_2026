my_name = "Alex"
my_surname = "Rudyk"

# конкатенація
full_name = my_name + " " + my_surname
print(full_name)

# f string
f_name = f"My name is {my_name}, my surname is {my_surname}"
print(f_name)

# * option
print(my_name*5)

print(id(my_name))
print(id(my_surname))
print(id(full_name))
print(id(f_name))

# format digits

pi = 3.14159265359
print(f"{pi:.2f}")