class Car:

    class_name = "Car class" #class atribute

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.tank = 0

    def set_tank(self, value): # class method
        self.tank = value

x5 = Car(brand="BMW", model="X5") #instance
print(x5.brand)
print(x5.model)

polo = Car(brand="VW", model= "Polo") #instance
print(polo.brand)
print(polo.model)

polo.tank = 50
print(polo.tank)

polo.set_tank(100)
print(polo.tank)

print(x5.tank)

print(x5.class_name)
print(polo.class_name)