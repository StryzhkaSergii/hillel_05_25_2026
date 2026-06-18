#set hash values uniq elements

my_set = {3,3,2,5,7}

print(my_set)

# we will get error
# my_set = {1, [1,2]}

my_set.add(4)
my_set.add(3)
print(my_set)

some_variable = my_set.pop()
print(some_variable)
print(my_set)

my_set.remove(7)
print(my_set)

# my_set.remove(None)

list_of_ids = [1001, 1001, 1356, 1002]
len_list = len(list_of_ids)
len_set = len(set(list_of_ids))

print(len_list == len_set)

actual_list_of_users = ["Alex", "Den", "Ivan"]
expected_list_of_users = ["Alex", "Ivan", "Den"]

print(actual_list_of_users == expected_list_of_users)
print(set(actual_list_of_users) == set(expected_list_of_users))