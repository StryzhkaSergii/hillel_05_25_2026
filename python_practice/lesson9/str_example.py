import logging

class User:
    def __init__(self, name, password, site_url): #constructor
        self.name = name
        self.password = password
        self.url = site_url

    def __str__(self):
        return f"User: {self.name}, url: {self.url}"

    def __repr__(self):
        return f"User(name='{self.name}', password='{self.password}', url='{self.url}')"

user = User("Alex", "alex_password", "google.com")
# str_user = str(user)
# # without __str__ -> <__main__.User object at 0x00000214948AB4D0>
# print(user)
# print(str_user)

# print(repr(user))
logging.error(repr(user))