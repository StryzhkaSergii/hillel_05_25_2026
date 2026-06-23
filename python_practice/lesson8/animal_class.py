class Animal:
    def make_sound(self):
        print("Animal sound")

    def go_sleep(self):
        print("Sleeping...")

    # def dog_sound(self):
    #     print("Grrr")
    #
    # def cat_sound(self):
    #     print("Meow")

class Dog(Animal): #наслідування
    def make_sound(self): #поліморфізм
        print("Grrr")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

class Bug(Animal):
    pass

# dog = Animal()
# cat = Animal()
dog = Dog()
cat = Cat()
unknown_animal = Animal()
bug= Bug()

dog.make_sound()
cat.make_sound()
unknown_animal.make_sound()
bug.make_sound()
# dog.dog_sound()
# cat.cat_sound()

dog.go_sleep()
cat.go_sleep()
bug.go_sleep()