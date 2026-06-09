my_list_names = ["Alex", "Den", "Ivan", "Viktor", "Sofa"]
my_list_ages = [1, 5, 18, 7, 95]

sorted_names = sorted(my_list_names)
sorted_ages = sorted(my_list_ages)

print(sorted_names)
print(sorted_ages)
print(id(my_list_ages))

sorted_names_reverse = sorted(my_list_names, reverse=True)
sorted_ages_reverse = sorted(my_list_ages, reverse=True)

print(sorted_names_reverse)
print(sorted_ages_reverse)

# print(my_list_names)
# print(my_list_ages)
#
# # змінює першочерговий список
#
# my_list_names.sort()
# my_list_ages.sort()
#
# print(my_list_names)
# print(my_list_ages)

def my_fn(word):
    word_lenth = len(word)
    return word_lenth

# lambda arg: action with arg
sorted_names_custom_lambda = sorted(my_list_names, key=lambda x: len(x))
sorted_names_custom = sorted(my_list_names, key=my_fn)

print(sorted_names_custom_lambda)
print(sorted_names_custom)



