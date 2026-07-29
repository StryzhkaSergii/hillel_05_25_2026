class SimpleNumbersIterator:
    def __init__(self, quantity_simple_numbers):
        self.quantity_simple_numbers = quantity_simple_numbers
        self.__current_num = 2
        self.__quantity_returned = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.__quantity_returned == self.quantity_simple_numbers:
            raise StopIteration
        self.__quantity_returned = self.__quantity_returned + 1
        self.__get_simple_number()
        return self.__current_num

    def __get_simple_number(self):
        while True:
            self.__current_num += 1
            if self.__is_prime(self.__current_num):
                return self.__current_num

    def __is_prime(self, number):
        for k in range(2, number - 1):
            if number % k == 0:
                return False
        return True

for el in SimpleNumbersIterator(15):
    print(el)