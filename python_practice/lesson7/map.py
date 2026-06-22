my_description = "My    name    is    Alex".split(" ")
print(my_description)
print(list(filter(len, my_description)))
print(list(map(len, my_description)))

print(pow(2, 5))
base_numbers = [2, 4, 6, 8, 10, 1000]
powers = [1, 2, 3, 4, 5]

result_of_map = list(map(pow, base_numbers, powers))
print(result_of_map)