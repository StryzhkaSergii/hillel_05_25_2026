#iter()
#next()

list_of_numbers = [11,12,13,14,15]
list_of_numbers2 = [21,22,23,24,25]

for el in range(10):
    print(el)

iter_object = iter(list_of_numbers)
iter_object2 = iter(list_of_numbers2)
print(type(iter_object))

# print(next(iter_object)) #0
# print(next(iter_object)) #1
# print(next(iter_object2))
# print(next(iter_object)) #2
# print(next(iter_object)) #3
# print(next(iter_object2))
# print(next(iter_object2))
# print(next(iter_object)) #4
# print(next(iter_object2))
# # print(next(iter_object2))
# print(iter_object2.__next__())
# print(next(iter_object)) #StopIteration exception

try:
    while True:
        print(next(iter_object))
except StopIteration:
    pass