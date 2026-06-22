# def sum_all_elements(list_elements):
#     return sum(list_elements)

# def sum_all_elements(number1, number2, number3):
#     return sum([number1, number2, number3])

# *args
# **kwargs
def sum_all_elements(double_arg, *args, ignore_arg=5, **kwargs):
    print("double arg: ", double_arg)
    print("Numbers: ", args)
    print("ignore number: ", ignore_arg)
    print("kwargs:", kwargs)
    numbers = [k for k in args if k != ignore_arg]
    result = sum(numbers) + double_arg * 2
    if kwargs.get("double_all") == True:
        result = result * 2
    return result

my_arguments = {"arg1": "value", "double_all": True, "additional_list" : [1,2,3]}
# print(sum_all_elements(1, 2, 3, 2, 5, *[41, 2, 5], ignore_arg=5))
print(sum_all_elements(1, 2, 3, 2, 5, *[41, 2, 5]))
print(sum_all_elements(1, 2, 3, 2, 5, *[41, 2, 5], ignore_arg=41, **my_arguments))