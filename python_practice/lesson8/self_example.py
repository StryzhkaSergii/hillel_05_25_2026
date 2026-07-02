class Auto:
    def __init__(self,model, color, engine, fuel_to_km=0.2):
        self.model = model
        self.color = color
        self.engine = engine
        self.__tank = 0
        self.__fuel_to_km = fuel_to_km

    def drive_to_nearest_town(self, distance_km):
        if self.__tank / self.__fuel_to_km >= distance_km:
            self.__tank = self.__tank - distance_km*self.__fuel_to_km
            print("Driving...")
        else:
            print(f"Can't go there, have fuel only on {self.__tank/self.__fuel_to_km} km")

    def set_tank(self, value):
        self.__tank = value

    def check_current_tank(self):
        return self.__tank

class Nissan(Auto):
    brand = "NISSAN"

    @classmethod
    def say_greeting(cls):
        print(f"Hello from {cls.brand}")






y61 = Nissan(model="y61", color="green", engine="3.0", fuel_to_km=0.1)
navara = Nissan(model="navara", color="red", engine="5.0")

print(y61.model)
print(navara.model)
y61.set_tank(50)
y61.drive_to_nearest_town(400)
y61.drive_to_nearest_town(400)
print(y61)

print(y61.check_current_tank())
navara.tank = 10
navara.drive_to_nearest_town(300)
Nissan.brand = "New Nissan"
navara.__class__.brand = "New Nissan"
print(navara.brand)
print(y61.brand)

navara.say_greeting()
Nissan.say_greeting()