import random
import time

from sqlalchemy import create_engine, func
from sqlalchemy.orm import declarative_base
from core.db.models.user import ORMUser
from sqlalchemy.orm import sessionmaker
from faker import Faker
from core.db.models.base import Base


# З'єднання з базою даних PostgreSQL
# Потрібно вказати правильні дані для вашої бази даних
POSTGRESQL_URL = "postgresql://postgres:2410ghjnjy@localhost:5432/hillel_05_25_2026"
SQLITE_URL = "sqlite:///path_to_db/my_sqlite.db"
engine = create_engine(POSTGRESQL_URL)

# Створюємо об'єкт сесії
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine) #створюємо таблицю з об'єкта ORMUser
# Додавання нового користувача
# new_user = ORMUser(name='John', age=30)
# session.add(new_user)
# session.commit()
# Відповідає INSERT INTO users (name, age) VALUES ('John', 30);

faker = Faker()
# for k in range(5):
#     session.add(ORMUser(name=f"{faker.name()}-{time.time()}", age= random.randint(18,100)))
#
# session.commit()

# select * from orm_users
all_users = session.query(ORMUser).all()
print(*all_users, sep="\n")
print(all_users[5].name)

# select count()
count_users = session.query(func.count(ORMUser.id)).first()
print(count_users)

# select * from table where age<=40
user_less_40 = session.query(ORMUser).filter(ORMUser.age <= 40).all()
age_24 = session.query(ORMUser).filter_by(age=24).first()

print(*user_less_40, sep="\n")
print(age_24)
# # Оновлення інформації про користувача
user = session.query(ORMUser).filter_by(name='John').first()
user.age = 31
# # Відповідає UPDATE users SET age=31 WHERE name='John';
#
# # Видалення користувача
# user_13 = session.query(ORMUser).filter_by(id=13).first()
# session.delete(user_13)

retired_users = session.query(ORMUser).filter(ORMUser.age>60).all()
for k in retired_users:
    session.delete(k)

session.commit()
session.close()
# # Відповідає DELETE FROM users WHERE name='John';