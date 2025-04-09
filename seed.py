import random
from faker import Faker
from models import Student, Group, Teacher, Subject, Grade
from connect import Session

# Init faker instance
faker = Faker()

# Const for list length
NUM_GROUPS = 3
NUM_TEACHERS = 5
NUM_SUBJECTS = 8
NUM_STUDENTS = 50
MAX_GRADES_PER_STUDENT = 20


def seed_data():
    session = Session()
    try:
        # Clear tables
        session.query(Grade).delete()
        session.query(Student).delete()
        session.query(Subject).delete()
        session.query(Teacher).delete()
        session.query(Group).delete()
        session.commit()

        # Create groups
        groups = []
        for i in range(NUM_GROUPS):
            group_name = f"Group {i+1}"
            groups.append(Group(name=group_name))

        session.add_all(groups)
        session.commit()

        print(f"Groups {len(groups)} created!")

        # Create teachers
        teachers = [Teacher(name=faker.name()) for _ in range(NUM_TEACHERS)]
        session.add_all(teachers)
        session.commit()

        print(f"Teachers {len(teachers)} created!")

        # Create subjects
        subjects = [
            Subject(name=faker.word().capitalize(), teacher=random.choice(teachers))
            for _ in range(NUM_SUBJECTS)
        ]
        session.add_all(subjects)
        session.commit()

        print(f"Subjects {len(subjects)} created!")

        # Create students
        students = [
            Student(name=faker.name(), group=random.choice(groups))
            for _ in range(NUM_STUDENTS)
        ]
        session.add_all(students)
        session.commit()

        print(f"Students {len(students)} created!")

        # Create grades
        grades = []
        for student in students:
            for _ in range(random.randint(1, MAX_GRADES_PER_STUDENT)):
                grade = Grade(
                    student=student,
                    subject=random.choice(subjects),
                    grade=random.randint(1, 5),
                    date=faker.date_between(start_date="-2y", end_date="today"),
                )
                grades.append(grade)

        session.add_all(grades)
        session.commit()

        print(f"Grades {len(grades)} created!")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()


if __name__ == "__main__":
    seed_data()
