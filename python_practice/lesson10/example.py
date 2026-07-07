# Опишіть об’єкт «Поїзд». Клас повинен містити поля та метод для додавання вагонів
# (необхідно додати об’єкти та екземпляри класу вагонів).
#
# В поїзді завжди є 1 вагон і це локомотив(він не приймає пасажирів)
# Опишіть клас Вагон разом із поїздом. Вагон повинен містити список пасажирів і дозволяти додавати пасажирів.
# У Вагоні може бути не більше 10 пасажирів.
#
# Під час використання функції len у вагоні я хочу бачити кількість пасажирів.
# Використовуючи len у поїзді, я хочу бачити список вагонів без локомотива. Кожен вагон повинен мати номер.

class Train:
    def __init__(self):
        self.locomotive = Wagon(is_locomotive=True, number=1)
        self.wagons = []

    def __len__(self):
        return len(self.wagons)

    def __str__(self):
        return f"Train with {len(self.wagons)} wagons: {', '.join([str(k) for k in self.wagons])}"

    def add_wagon(self, wagon: Wagon):
        # current_wagon = len(self.wagons) + 1

        if wagon.number not in [k.number for k in self.wagons]:
            self.wagons.append(wagon)




class Wagon:
    def __init__(self, number, is_locomotive=False):
        self.is_locomotive = is_locomotive
        self.number = number
        if not self.is_locomotive:
            self.passengers = []
        # self.is_excepting_passengers = True

    def __str__(self):
        return f"Wagon # {self.number}, is locomotive {self.is_locomotive}"

    def __len__(self):
        return len(self.passengers)

    def add_passengers(self, passenger: dict):
        if len(self.passengers) is not 10:
            self.passengers.append(passenger)
        pass

train = Train()
print(train)
wg1 = Wagon(number=2)
wg1.add_passengers({"name": "Alex", "pass_number": "#18557"})

train.add_wagon(wg1)
train.add_wagon(wg1)
print(wg1.passengers)
print(train)
# wagon = Wagon(number=2, is_locomotive=False)