class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    # def __del__(self):
    #     print(f"The {self.make} {self.model} object has been destroyed.")
# Створення об'єкта та автоматичний виклик конструктора
my_car = Car("Toyota", "Camry")

print(my_car.make)  # Виведе: Toyota
print(my_car.model) # Виведе: Camry

del my_car