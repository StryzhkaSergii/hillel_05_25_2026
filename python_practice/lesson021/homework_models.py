from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    courses = relationship(
        "Course",
        secondary="student_course",
        back_populates="students"
    )


class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    students = relationship(
        "Student",
        secondary="student_course",
        back_populates="courses"
    )


class StudentCourse(Base):
    __tablename__ = "student_course"

    student_id = Column(
        Integer,
        ForeignKey("students.id"),
        primary_key=True
    )

    course_id = Column(
        Integer,
        ForeignKey("courses.id"),
        primary_key=True
    )