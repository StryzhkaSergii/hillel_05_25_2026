class User:
    def __init__(self, name, password, site_url, height): #constructor
        self.name = name
        self.password = password
        self.url = site_url
        self.finished_courses = []
        self.height = height

    # def __len__(self):
    #     return len(self.finished_courses)

    def __len__(self):
        return self.height

    def __eq__(self, other):
        if isinstance(other, User):
            return self.height == other.height or self.name == other.name
        return False

    def __gt__(self, other):
        if isinstance(other, User):
            return self.height > other.height
        return False

    def __ge__(self, other):
        if isinstance(other, User):
            return self.height >= other.height
        return False



user_alex = User("Alex", "alex_password", "google.com", 155)
user_den = User("Den", "alex_password", "google.com", 150)
user_alex.finished_courses.append("math")
user_alex.finished_courses.append("phil")
print(len(user_alex))


print(len(user_alex))
print(user_den.height == user_alex.height)

print(user_den == 180)

# print(user_den >= user_alex)
print(user_den > user_alex)
print(user_den < user_alex) # -> (not user_den > user_alex)