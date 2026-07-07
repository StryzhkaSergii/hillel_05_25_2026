class Animal:
    def make_sound(self):
        print("Animal sound")

    def walk(self):
        print("walking...")

    def __str__(self):
        return "Animal object"

class Lion(Animal):
    def __init__(self, name):
        self.name = name
        self.legs = 4
        self.tail = "Flufy"

    def make_sound(self):
        print("Rrrr")

class Bird(Animal):
    def __init__(self, name):
        self.name = name
        self.wings = 2

    def make_sound(self):
        print("Chiric")


class Hymera(Bird, Lion):

    def __init__(self, name):
        super().__init__(name)
        self.tail = "Sharp"
        self.legs = 4

        # self.name = name
        Lion.__init__(self,name)
        # Bird.__init__(self, name)

pushok = Hymera("Pushok")
print(pushok.name)
print(pushok.wings)
print(pushok.legs)
print(pushok.tail)
pushok.make_sound()
print(Hymera.mro())