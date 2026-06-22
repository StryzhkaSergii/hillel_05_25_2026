def greeting(first_name: str, second_name: str) -> None:
    print(f"Hello {first_name}, {second_name}")

def get_greeting(first_name: str, second_name: str) -> str:
    """
    This is DOC string example
    :param first_name: user first name
    :param second_name: user second name
    :return: full greeting
    """
    return f"Hello {first_name}, {second_name}"

def div_two_elements(first, second) -> float:
    return first / second
# for full_name in [("Oleksandr", "Rudyk"), ("John", "Dow")]:
#     greeting(full_name[0], full_name[1])

# for full_name in [("Oleksandr", "Rudyk"), ("John", "Dow")]:
#     greeting(full_name[0], full_name[1])

# print(div_two_elements("10",5))