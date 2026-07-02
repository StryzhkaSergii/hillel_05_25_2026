class Rhombus:
    def __init__(self, storona_a, kut_a):
        self.storona_a = storona_a
        self.kut_a = kut_a

    def __setattr__(self, name, value):
        if name == "storona_a":
            if value <= 0:
                raise ValueError("Довжина сторони повинна бути більшою за 0.")
            super().__setattr__(name, value)
        elif name == "kut_a":
            if not (0 < value < 180):
                raise ValueError("Кут повинен бути між 0 і 180 градусів.")
            super().__setattr__(name, value)

            super().__setattr__("kut_b", 180 - value)
        elif name == "kut_b":
            raise AttributeError("Значення кута_b встановлюється автоматично через кут_а.")
        else:
            super().__setattr__(name, value)

    def __str__(self):
        return f"Ромб: сторона a = {self.storona_a}, кут a = {self.kut_a}, кут b = {self.kut_b}"


romb = Rhombus(5, 60)
print(romb)