import pathlib
from constants import BASE_PROJECT_PATH
import os
import shutil

current_dir = pathlib.Path().absolute()
root_dir = pathlib.Path().absolute().parent.parent

test_folder_path = pathlib.Path(os.path.join(str(current_dir), "test_folder"))
tree_test_folder_path = pathlib.Path(os.path.join(str(current_dir), "first_folder\\second_folder\\final_folder"))
tree_test_folder_path_copy = pathlib.Path(os.path.join(str(current_dir), "first_folder"))
# print(test_folder_path)
# print("is exist = ",test_folder_path.exists())
#
# test_folder_path.mkdir(exist_ok=True)
# print("is exist = ",test_folder_path.exists())
# test_folder_path.rmdir()
# print("is exist = ",test_folder_path.exists())

# print(tree_test_folder_path)
# print("is exist = ",tree_test_folder_path.exists())
#
# tree_test_folder_path.mkdir(exist_ok=True, parents=True)
# print("is exist = ",tree_test_folder_path.exists())

# shutil.rmtree(path=tree_test_folder_path_copy)
# print("is exist = ",tree_test_folder_path_copy.exists())

os.remove(os.path.join(str(current_dir), "file_for_read_write.txt"))