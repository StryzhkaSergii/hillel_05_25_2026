import pathlib
from constants import BASE_PROJECT_PATH
import os

current_dir = pathlib.Path().absolute()
root_dir = pathlib.Path().absolute().parent.parent

# print(type(current_dir))
# print(current_dir)
# print(current_dir.name)
# print(current_dir.parent)

parents = current_dir.parents

# for par in parents:
#     print(par.name)

# for path_ in current_dir.iterdir():
#     if path_.is_file():
#         print(path_.name)
# print("-"*80)
# for path_ in current_dir.iterdir():
#     if path_.is_dir():
#         print(path_.name)

# for path_ in root_dir.iterdir():
#     if path_.is_file():
#         print(path_.name)
# print("-"*80)
# for path_ in root_dir.iterdir():
#     if path_.is_dir():
#         print(path_.name)



# lesson4_full_path = os.path.join(str(current_dir.parent), "lesson4")
# print(lesson4_full_path)
#
# for path_ in pathlib.Path(lesson4_full_path).iterdir():
#     if path_.is_file():
#         print(path_.name)
# print("-"*80)
# for path_ in pathlib.Path(lesson4_full_path).iterdir():
#     if path_.is_dir():
#         print(path_.name)

file_to_find = "join_example.py"

for current_path, folders, files in os.walk(BASE_PROJECT_PATH):
    if file_to_find in files:
        print(os.path.join(current_path,file_to_find))

print("-"*80)

partial_file_name = "string"

for current_path, folders, files in os.walk(BASE_PROJECT_PATH):
    for file in files:
        if partial_file_name in file:
            print(os.path.join(current_path,file))