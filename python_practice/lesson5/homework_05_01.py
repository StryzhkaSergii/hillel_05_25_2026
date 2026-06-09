people_records = [
    ('John', 'Doe', 28, 'Engineer', 'New York'),
    ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
    ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
    ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
    ('Michael', 'Brown', 22, 'Student', 'Seattle'),
    ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
    ('David', 'Miller', 33, 'Software Developer', 'Austin'),
    ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
    ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
    ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
    ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
    ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
    ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
    ('Ava', 'White', 42, 'Journalist', 'San Diego'),
    ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

my_record = ('Andrii', 'Shevchenko', 40, 'Footballer', 'Kyiv')  # Додаємо новий запис на початок списку
people_records.insert(0, my_record)
print(people_records)

people_records[1], people_records[5] = people_records[5], people_records[1]  # Обмінюємо елементи з індексами 1 і 5
print("Modified list:")
print(people_records)

indexes_to_check = [6, 10, 13]  # Перевіряємо, чи всі люди з індексами 6, 10, 13 мають вік ≥ 30
condition = all(people_records[i][2] >= 30 for i in indexes_to_check)
print("All ages >= 30 at indexes 6, 10, 13:", condition)