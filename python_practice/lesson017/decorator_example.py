# def greeting(name):
#     print(f"Hi {name}")
#
# def greeting2(name):
#     print(f"Hello {name}")
#
# def good_morning(fn,name):
#     print("Good morning!")
#     fn(name)
#
#
# good_morning(greeting, "Alex")
# good_morning(greeting2, "Alex")
# greeting("Alex")
#
# my_new_func = greeting
# my_new_func("Den")
# print(id(greeting))
# print(id(my_new_func))

def greeting_decorator(function):
    def wrapper(*args, **kwargs):
        print("Good morning")
        return function(*args, **kwargs)
    return wrapper

@greeting_decorator
def greeting(name):
    print(f"Hi {name}")

@greeting_decorator
def something_else(list_, age):
    for el in list_:
        print(el+age)



greeting('Alex')

something_else([20,10,30], 5)