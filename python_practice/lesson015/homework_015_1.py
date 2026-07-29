# Зберігаємо унікальні рядки
unique_lines = set()

# Читаємо перший файл
with open("r-m-c.csv", "r", encoding="utf-8") as file1:
    header = file1.readline()      # Зчитуємо заголовок
    unique_lines.update(file1.readlines())

# Читаємо другий файл
with open("rmc.csv", "r", encoding="utf-8") as file2:
    file2.readline()               # Пропускаємо заголовок
    unique_lines.update(file2.readlines())

# Записуємо результат
with open("result_stryzhka.csv", "w", encoding="utf-8") as result:
    result.write(header)           # Записуємо заголовок
    result.writelines(sorted(unique_lines))

print("Файл result_stryzhka.csv успішно створено.")
print(f"Унікальних записів: {len(unique_lines)}")