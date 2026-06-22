def is_even(number):
    return number % 2 == 0
result_list = []
for elem in range(20):
    if is_even(elem):
        result_list.append(elem)
print(result_list)

print([num for num in range(20) if is_even(num)])
print(list(filter(is_even, range(20))))

my_description = "My    name    is    Alex".split(" ")
print(my_description)
result = []
for k in my_description:
    if len(k):
        result.append(k)

print(result)
print(list(filter(len, my_description)))
print([k for k in my_description if len(k)])

filtered_list = list(filter(len, my_description))
print(filtered_list[0])
print(my_description)