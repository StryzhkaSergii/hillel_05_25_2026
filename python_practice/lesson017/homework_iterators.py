class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration

        value = self.data[self.index]
        self.index -= 1
        return value

# Приклад використання
numbers = [10, 20, 30, 40, 50]

for num in ReverseIterator(numbers):
    print(num)


#Ітератор парних чисел від 0 до N
class EvenIterator:
    def __init__(self, n):
        self.n = n
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.n:
            raise StopIteration

        value = self.current
        self.current += 2
        return value


# Приклад використання
for number in EvenIterator(10):
    print(number)