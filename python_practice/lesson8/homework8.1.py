class Student:
    def __init__(self, first_name, last_name, age, average_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def update_average_grade(self, new_grade):
        self.average_grade = new_grade

    def show_info(self):
        print(f"Ім'я: {self.first_name}")
        print(f"Прізвище: {self.last_name}")
        print(f"Вік: {self.age}")
        print(f"Середній бал: {self.average_grade}")


student = Student("Іван", "Петренко", 20, 85)

print("Початкова інформація:")
student.show_info()

student.update_average_grade(92)

print("\nПісля зміни середнього балу:")
student.show_info()
