from python_practice.lesson9.str_example import User

user = User("Alex", "alex_password", "google.com")
str_user = str(user)
# without __str__ -> <__main__.User object at 0x00000214948AB4D0>
print(user)
print(str_user)