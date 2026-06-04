string_example = "Text"
string_example_ukr = "Текст українською"

print(string_example)
print(string_example_ukr)

print(id(string_example))

copy_string = string_example
print(id(copy_string))
copy_string = "Some new string"
print(id(copy_string))
