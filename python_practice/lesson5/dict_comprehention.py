import random
dct_cmp = {number: number**2 for number in range(10)}
print(dct_cmp)

names = ["Alex", "Den", "Ivan", "Sofa", "Viktor"]
dict_with_names = {number: random.choice(names) for number in range(10)}
print(dict_with_names)