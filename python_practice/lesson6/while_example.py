import random

while True: # вічний цикл
    number = random.random() # випадкове число від 0 до 1
    print(number)

    if number > 0.5:
        break