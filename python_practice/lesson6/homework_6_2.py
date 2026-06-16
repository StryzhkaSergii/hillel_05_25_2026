word = input("Введіть слово: ")

while "h" not in word and "H" not in word:
    word = input("У слові немає літери h. Спробуйте ще раз: ")

print("Дякую!")