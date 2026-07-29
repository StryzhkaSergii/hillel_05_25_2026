class SimpleRangeIterator:
    def __init__(self, max_number):
        self.__current = -1
        self.max_number = max_number

    def __next__(self):

        self.__current = self.__current + 1
        if self.__current == self.max_number:
            raise StopIteration
        return self.__current

    def __iter__(self):
        return self

for el in SimpleRangeIterator(10):
    print(el)