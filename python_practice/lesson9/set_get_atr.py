class User:
    def __init__(self, name, score): #constructor
        self.name = name
        self.score = score

    def __str__(self):
        return f"User: {self.name}, score: {self.score}"

    def __setattr__(self, key, value):
        if key == 'score':
            if not (100 >= value >= 0):
                print("score must be between 0 and 100. Set 0")
                value = 0
        super.__setattr__(self, key, value)

alex = User("Alex", -50)
alex.score = -50
print(alex)