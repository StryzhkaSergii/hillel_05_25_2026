file_path = "file_for_read_write.txt"

# r - reading, читання файлу
# w - режим запису/перестворення файлу
# a - append, додавання в файл, створиться якщо выдсутній

# r+ - read + write, file should exist
# w+ - read + write, file can be absent
# a+ - read + append, file can be absent

with open(file_path, mode="w") as f:
    f.write("line1\n")
    f.write("line2\n\t")
    f.write(r"line3\n") #raw string
    f.write(" lin\"e4\\\n")
    f.write(file_path)
    f.write("ERROR")
    f.write("""\n\n first row
    second row
last row\n""")
    f.writelines(["writelines1\n", "writelines2\n", "writelines3"])

# with open(file_path, mode="a") as f:
#     f.write("line3\n")
#     f.write("line4\n")

with open(file_path, mode="r") as f:
    data = f.read()
    print(data)
    data2 = f.read()
    print("-"*80)
    print(data2)

with open(file_path, mode="r") as f:
    data = f.readlines()
    print(data)

with open(file_path, mode="r") as f:
    while True:
        line = f.readline()
        if "ERROR" in line:
            print(line)
            break
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print(f.readline())
    # print("-" * 80)
    # print(f.readlines())