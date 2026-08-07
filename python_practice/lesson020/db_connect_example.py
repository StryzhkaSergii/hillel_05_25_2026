import psycopg2

# Параметри підключення
# База даних повинна існувати на зазначеному хості, та юзер повинен мати право на читання цього запису
dbname = 'hillel_05_25_2026'
user = 'postgres'
password = '2410ghjnjy'
host = '127.0.0.1'
port = '5432'

# Спроба підключитись до бази даних
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
    cursor.execute("SELECT * FROM public.users")

    # Отримання результатів запиту
    records = cursor.fetchall()
    print(records)
    cursor.execute("SELECT * FROM public.users WHERE id=1")
    record = cursor.fetchone()
    print(record)
    cursor.execute("""insert into public.users ("name") values ('Den');""")
    connection.commit() #механізм підтвердження транзакції


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)

finally:
    # Закриваємо підключення
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")