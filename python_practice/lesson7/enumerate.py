for k in enumerate(["den", "alex"]):
    print(k)

for k in enumerate(["den", "alex"], start=15):
    print(k)

for index, name in enumerate(["den", "alex"], start=15):
    print(f"Name {name}, index: {index}")
# print(type(enumerate(["den", "alex"])))