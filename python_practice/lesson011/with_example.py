with open("example.txt") as f: #менеджер контексту
    print(f.read())

print("Do something else")

try:
    f = open("example.txt") #__enter__
    print(f.read())
finally:
    f.close() #__exit__