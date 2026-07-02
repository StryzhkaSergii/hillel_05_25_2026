class Car:
    def __init__(self, make, model):
        self.make = make          # Public attribute
        self._model = model        # Protected attribute
        self.__year = 2022         # Private attribute

    def display_model(self):
        print(f"Model: {self._model}")

    def set_year(self, new_year):
        self.__year = new_year

    def get_year(self):
        return self.__year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

car = Car("tesla", "model s")
car.set_year(2020)
print(car.get_year())

print(car.year)
car.year = 2026
print(car.year)