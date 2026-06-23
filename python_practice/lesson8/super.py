class Vehicle:
    def __init__(self, color):
        self.color = color

class Car(Vehicle):
    def __init__(self, color, model, wheels):
        # self.color = color
        super().__init__(color)
        self.model = model
        self.wheels = wheels

my_car = Car(color="Blue", model="Honda", wheels=4)
another_car = Car(color="Gree", model="Honda", wheels=4)
print(my_car.wheels)  # Виведе "4"
print(my_car.color)