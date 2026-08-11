import psycopg2
import traceback
import json
from decimal import Decimal

# Параметри підключення
# База даних повинна існувати на зазначеному хості, та юзер повинен мати право на читання цього запису
dbname = 'hillel_05_25_2026'
user = 'postgres'
password = 'postgres'
host = '127.0.0.1'
port = '5432'

try:
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    print("Connected to the database successfully!")

    # Для виконання запитів ви можете створити курсор
    cursor = connection.cursor()

    # Для виконання SQL запитів ви можете викликати метод execute() курсора
    # Тут можна виконати будь який запит на мові SQL, і він виконається в БД
    # cursor.execute("""INSERT INTO public.categories (name) VALUES
    # ('Electronics'),
    # ('Clothing'),
    # ('Books')""")
    # records_insert = cursor.fetchall()
    # print(records_insert)

    cursor.execute("SELECT * FROM public.categories")
    records = cursor.fetchall() # Отримання результатів запиту, якщо багато
    print(records)

    cursor.execute("SELECT * FROM public.categories WHERE id=1")
    record = cursor.fetchone() # Отримання результатів запиту, якщо один
    print(record)

    # cursor.execute("""INSERT INTO public.products (name, description, price, category_id) VALUES
    # ('Smartphone', 'Latest model with high-resolution camera', 799.99, 1),
    # ('Laptop', 'Lightweight laptop with long battery life', 1299.99, 1),
    # ('T-shirt', 'Cotton t-shirt with various designs', 19.99, 2),
    # ('Jeans', 'Comfortable and stylish jeans', 49.99, 2),
    # ('Novel', 'Best-selling fiction book', 14.99, 3),
    # ('Textbook', 'Guide to advanced programming concepts', 69.99, 3)""")
    # records_insert1 = cursor.fetchall()
    # print(records_insert1)

    try:
        cursor.execute("""insert into public.categories ("name") values ('Phones');""")
        connection.commit() #механізм підтвердження транзакції
    except psycopg2.errors.UniqueViolation:
        connection.rollback()  # скидаємо "зіпсовану" транзакцію
        print("Category 'Phones' already exists, skipping insert")

    # або
    # category_name = 'Phones'  # Тут значення змінюється динамічно
    #
    # try:
    #     # Виконуємо SQL-запит із параметром для категорії
    #     cursor.execute("""INSERT INTO public.categories ("name") VALUES (%s);""", (category_name,))
    #     connection.commit()  # Механізм підтвердження транзакції
    # except psycopg2.errors.UniqueViolation:
    #     connection.rollback()  # Скидаємо "зіпсовану" транзакцію
    #     print(f"Category '{category_name}' already exists, skipping insert")

    cursor.execute("""SELECT 
    products.name AS product_name,
    products.description,
    products.price,
    categories.name AS category_name
FROM 
    products
JOIN 
    categories
ON 
    products.category_id = categories.id""")
    join_records = cursor.fetchall()  # Отримання результатів запиту
    # print(join_records)

    # Форматування даних у JSON
    columns = ["product_name", "description", "price", "category_name"]
    json_data = [dict(zip(columns, row)) for row in join_records]

    # Вивід даних у форматі JSON
    print(json.dumps(json_data, indent=4, default=lambda o: float(o) if isinstance(o, Decimal) else str(o)))

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
    traceback.print_exc()  # покаже файл, номер рядка та рядок коду, де сталась помилка

finally:
    # Закриваємо підключення
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")