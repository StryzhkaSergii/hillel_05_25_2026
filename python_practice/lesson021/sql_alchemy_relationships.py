from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from core.db.base import Base

from core.db.models.department import Department
from core.db.models.employee import Employee

# З'єднання з базою даних PostgreSQL (замініть дані на ваші)
POSTGRESQL_URL = "postgresql://postgres:2410ghjnjy@localhost:5432/hillel_05_25_2026"
engine = create_engine(POSTGRESQL_URL)

# Створення базового класу для визначення моделей даних
Base = declarative_base()

# Визначення моделей даних (таблиць) за допомогою класів


# Створення таблиць у базі даних
Base.metadata.create_all(engine)

# Створення сесії для взаємодії з базою даних
Session = sessionmaker(bind=engine)
session = Session()

# Додавання департаментів та співробітників до бази даних
it_department = Department(name='IT')
hr_department = Department(name='HR')

john = Employee(name='John', department=it_department)
alice = Employee(name='Alice', department=hr_department)
bob = Employee(name='Bob', department=it_department)

session.add_all([it_department, hr_department, john, alice, bob])
session.commit()

# Вибірка співробітників та їх департаментів
employees = session.query(Employee).all()
for employee in employees:
    print(f"Ім'я: {employee.name}, Департамент: {employee.department.name}")

# Закриття сесії
session.close()