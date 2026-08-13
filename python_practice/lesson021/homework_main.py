from random import sample

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from python_practice.lesson021.homework_models import Base, Student, Course


# З'єднання з базою даних PostgreSQL
POSTGRESQL_URL = (
    "postgresql://postgres:postgres@localhost:5432/hillel_05_25_2026"
)

engine = create_engine(POSTGRESQL_URL)


# Створення таблиць у базі даних
Base.metadata.create_all(engine)


# Створення сесії
Session = sessionmaker(bind=engine)
session = Session()


# 1. Створення 5 курсів

python = Course(name="Python")
sql = Course(name="SQL")
qa = Course(name="QA Testing")
automation = Course(name="Automation")
git = Course(name="Git")

courses = [
    python,
    sql,
    qa,
    automation,
    git
]

session.add_all(courses)
session.commit()


# 2. Створення 20 студентів

students = []

for i in range(1, 21):

    student = Student(
        name=f"Student {i}",
        email=f"student{i}@example.com"
    )

    # Випадково призначаємо від 1 до 3 курсів
    student.courses = sample(courses, k=sample([1, 2, 3], 1)[0])

    students.append(student)


session.add_all(students)
session.commit()

print("20 студентів створено та розподілено по курсах.")


# 3. Додавання нового студента

new_student = Student(
    name="John",
    email="john@example.com"
)

new_student.courses.append(python)

session.add(new_student)
session.commit()

print("\nНовий студент доданий:")
print(f"Ім'я: {new_student.name}")
print(f"Email: {new_student.email}")
print(f"Курс: {python.name}")


# 4. Студенти певного курсу

print("\nСтуденти курсу Python:")

python_students = session.query(Student).filter(
    Student.courses.any(Course.name == "Python")
).all()

for student in python_students:
    print(
        f"Ім'я: {student.name}, "
        f"Email: {student.email}"
    )

# 5. Курси певного студента

student = session.query(Student).filter_by(
    name="Student 1"
).first()

print(f"\nКурси студента {student.name}:")

for course in student.courses:
    print(course.name)


# 6. Оновлення даних студента

student = session.query(Student).filter_by(
    name="Student 1"
).first()

student.name = "Updated Student"
student.email = "updated@example.com"

session.commit()

print("\nДані студента оновлено.")


# 7. Додавання студента на додатковий курс

student = session.query(Student).filter_by(
    name="Updated Student"
).first()

sql_course = session.query(Course).filter_by(
    name="SQL"
).first()

student.courses.append(sql_course)

session.commit()

print("Студента додано на курс SQL.")


# 8. Оновлення назви курсу

course = session.query(Course).filter_by(
    name="Git"
).first()

course.name = "Git & GitHub"

session.commit()

print("Назву курсу оновлено.")


# 9. Видалення студента

student = session.query(Student).filter_by(
    name="John"
).first()

if student:
    session.delete(student)
    session.commit()

    print("Студента John видалено.")


# 10. Перевірка всіх студентів

print("\nВсі студенти:")

students = session.query(Student).all()

for student in students:
    print(
        f"Ім'я: {student.name}, "
        f"Email: {student.email}"
    )


# Закриття сесії
session.close()