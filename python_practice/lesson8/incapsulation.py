class Car:

    class_name = "Car class" #class atribute

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.tank = 0

    def set_tank(self, value): # class method
        self.tank = value

    def go_somewhere(self, amount_in_km):
        if self.tank >= amount_in_km:
            self.tank = self.tank - amount_in_km
            print("Driving...")
        else:
            print("Can't go - have not enough fuel")

x5 = Car(brand="BMW", model="X5") #instance
x5.set_tank(50)
x5.go_somewhere(40)
x5.go_somewhere(40)
polo = Car(brand="VW", model= "Polo") #instance
polo.go_somewhere(10)