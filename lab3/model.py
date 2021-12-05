import random
import psycopg2


class Student:
    def __init__(self, connection, students):
        self.connection = connection
        self.students = students

    def add_student(self, line):
        try:
            line_inserting = line.split(", ")
            insert_query = self.students.insert().values(
                name=f'{line_inserting[0]}',
                age=line_inserting[1],
                grade=line_inserting[2]
            )
            self.connection.execute(insert_query)
        except:
            print("Error: student was not added!")

    def update_student(self, line):
        try:
            line_updating = line.split(", ")
            update_query = self.students.update().where(self.students.c.id == line_updating[0]).values(
                name=f'{line_updating[1]}',
                age=line_updating[2],
                grade=line_updating[3]
            )
            self.connection.execute(update_query)
        except:
            print("Error: student was not updated!")

    def delete_student(self, line_deleting):
        try:
            delete_query = self.students.delete().where(self.students.c.id == line_deleting)
            self.connection.execute(delete_query)
        except:
            print("Error: student was not deleted")


    def generate_random_students(self, number_of_lines):
        try:
            i = 0
            while i < number_of_lines:
                insert_query = self.students.insert().values(
                    name=f'{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}',
                    age=random.randint(5, 18),
                    grade=random.randint(1, 11)
                )
                self.connection.execute(insert_query)
                i += 1
        except:
            print("Error: student was not generated!")



class Teacher:
    def __init__(self, connection, teachers):
        self.connection = connection
        self.teachers = teachers

    def add_teacher(self, line):
        try:
            line_inserting = line.split(", ")
            insert_query = self.teachers.insert().values(
                name=f'{line_inserting[0]}',
                age=line_inserting[1],
                work_experience=line_inserting[2]
            )
            self.connection.execute(insert_query)
        except:
            print("Error: teacher was not added!")

    def update_teacher(self, line):
        try:
            line_updating = line.split(", ")
            update_query = self.teachers.update().where(self.teachers.c.id == line_updating[0]).values(
                name=f'{line_updating[1]}',
                age=line_updating[2],
                work_experience=line_updating[3]
            )
            self.connection.execute(update_query)
        except:
            print("Error: teacher was not updated!")

    def delete_teacher(self, line_deleting):
        try:
            delete_query = self.teachers.delete().where(self.teachers.c.id == line_deleting)
            self.connection.execute(delete_query)
        except:
            print(f"Error: teacher with id = {line_deleting} does not exist!")

    def generate_random_teachers(self, number_of_lines):
        try:
            i = 0
            while i < number_of_lines:
                insert_query = self.teachers.insert().values(
                    name=f'{chr(random.randint(65, 90))}{chr(random.randint(65, 90))}',
                    age=random.randint(25, 75),
                    work_experience=random.randint(0, 50)
                )
                self.connection.execute(insert_query)
                i += 1
        except:
            print("Error: teacher was not generated!")




class Subject:
    def __init__(self, connection, subjects):
        self.connection = connection
        self.subjects = subjects

    def create_trigger(self):
        con = psycopg2.connect(
            database='postgres',
            user='postgres',
            password=1234567890,
            host='localhost',
            port=5432,
        )
        create_trigger = """CREATE TRIGGER t_subject
        AFTER UPDATE OR DELETE ON subjects FOR EACH ROW EXECUTE PROCEDURE add_to_log ();"""
        con.autocommit = True
        cursor = con.cursor()
        cursor.execute(create_trigger)


    def add_subject(self, line):
        try:
            line_inserting = line.split(", ")
            insert_query = self.subjects.insert().values(
                name=f'{line_inserting[0]}',
                classes_per_semester=line_inserting[1]
            )
            self.connection.execute(insert_query)
        except:
            print("Error: subject was not added!")

    def update_subject(self, line):
        try:
            line_updating = line.split(", ")
            update_query = self.subjects.update().where(self.subjects.c.id == line_updating[0]).values(
                name=f'{line_updating[1]}',
                classes_per_semester=line_updating[2]
            )
            self.create_trigger()
            self.connection.execute(update_query)
        except:
            print("Error: subject was not updated!")

    def delete_subject(self, line_deleting):
        try:
            delete_query = self.subjects.delete().where(self.subjects.c.id == line_deleting)
            # self.create_trigger()
            self.connection.execute(delete_query)
        except:
            print(f"Error: subject with id = {line_deleting} does not exist!")

    def generate_random_subjects(self, number_of_lines):
        try:
            i = 0
            subject_name = ["literature", "math", "science", "art", "biology", "PE", "english", "french", "geography",
                            "history"]
            while i < number_of_lines:
                insert_query = self.subjects.insert().values(
                    name=f'{subject_name[random.randint(0, 9)]}',
                    classes_per_semester=random.randint(8, 80)
                )
                self.connection.execute(insert_query)
                i += 1
        except:
            print("Error: subject was not generated!")



class Subject_Teacher:
    def __init__(self, connection, subjects_teachers):
        self.connection = connection
        self.subjects_teachers = subjects_teachers

    def add_subjects_teachers_record(self, line):
        try:
            line_inserting = line.split(", ")
            insert_query = self.subjects_teachers.insert().values(
                subject_id=line_inserting[0],
                teacher_id=line_inserting[1]
            )
            self.connection.execute(insert_query)
        except:
            print("Error: record was not added!")

    def update_subjects_teachers_record(self, line):
        try:
            line_updating = line.split(", ")
            update_query = self.subjects_teachers.update().where(self.subjects_teachers.c.id == line_updating[0]).values(
                subject_id=line_updating[1],
                teacher_id=line_updating[2]
            )
            self.connection.execute(update_query)
        except:
            print("Error: record was not updated!")

    def delete_subjects_teachers_record(self, line_deleting):
        try:
            delete_query = self.subjects_teachers.delete().where(self.subjects_teachers.c.id == line_deleting)
            self.connection.execute(delete_query)
        except:
            print(f"Error: record with id = {line_deleting} does not exist!")

    def generate_random_subjects_teachers_records(self, number_of_lines):
        try:
            i = 0
            while i < number_of_lines:
                insert_query = self.subjects_teachers.insert().values(
                    subject_id=random.randint(1, 500),
                    teacher_id=random.randint(1, 500)
                )
                self.connection.execute(insert_query)
                i += 1
        except:
            print("Error: record was not generated!")




class Schedule:
    def __init__(self, connection, schedule):
        self.connection = connection
        self.schedule = schedule

    def add_schedule_record(self, line):
        try:
            line_inserting = line.split(", ")
            insert_query = self.schedule.insert().values(
                day=f'{line_inserting[0]}',
                time=f'{line_inserting[1]}',
                subject_teacher_id=line_inserting[2],
                student_id=line_inserting[3]
            )
            self.connection.execute(insert_query)
        except:
            print("Error: record was not added!")

    def update_schedule_record(self, line):
        try:
            line_updating = line.split(", ")
            update_query = self.schedule.update().where(self.schedule.c.id == line_updating[0]).values(
                day=f'{line_updating[1]}',
                time=f'{line_updating[2]}',
                subject_teacher_id=line_updating[3],
                student_id=line_updating[4]
            )
            self.connection.execute(update_query)
        except:
            print("Error: record was not updated!")

    def delete_schedule_record(self, line_deleting):
        try:
            delete_query = self.schedule.delete().where(self.schedule.c.id == line_deleting)
            self.connection.execute(delete_query)
        except:
            print(f"Error: record with id = {line_deleting} does not exist!")

    def generate_random_schedule_records(self, number_of_lines):
        try:
            i = 0
            days_of_week = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
            while i < number_of_lines:
                insert_query = self.schedule.insert().values(
                    day=days_of_week[random.randint(0, 5)],
                    time=f'{random.randint(8, 16)}:{random.randint(0, 59)}',
                    subject_teacher_id=random.randint(1, 500),
                    student_id=random.randint(2, 500)
                )
                self.connection.execute(insert_query)
                i += 1
        except:
            print("Error: record was not generated!")




class Mark:
    def __init__(self, connection, marks):
        self.connection = connection
        self.marks = marks

    def add_mark(self, line):
        try:
            line_inserting = line.split(", ")
            insert_query = self.marks.insert().values(
                student_id=line_inserting[0],
                subject_teacher_id=line_inserting[1],
                points=line_inserting[2]
            )
            self.connection.execute(insert_query)
        except:
            print("Error: mark was not added!")

    def update_mark(self, line):
        try:
            line_updating = line.split(", ")
            update_query = self.marks.update().where(self.marks.c.id == line_updating[0]).values(
                student_id=line_updating[1],
                subject_teacher_id=line_updating[2],
                points=line_updating[3]
            )
            self.connection.execute(update_query)
        except:
            print("Error: mark was not updated!")

    def delete_mark(self, line_deleting):
        try:
            delete_query = self.marks.delete().where(self.marks.c.id == line_deleting)
            self.connection.execute(delete_query)
        except:
            print(f"Error: mark with id = {line_deleting} does not exist!")

    def generate_random_marks(self, number_of_lines):
        try:
            i = 0
            while i < number_of_lines:
                insert_query = self.marks.insert().values(
                    student_id=random.randint(2, 500),
                    subject_teacher_id=random.randint(1, 500),
                    points=random.randint(1, 12)
                )
                self.connection.execute(insert_query)
                i += 1
        except:
            print("Error: marks were not generated!")




class Search:

    def __init__(self):
        self.connection = psycopg2.connect(
            database='postgres',
            user='postgres',
            password=1234567890,
            host='localhost',
            port=5432,
        )

    def find_subjects_teachers_records_by_name_classes_age(self, classes_range, subject_name, age_range):
        try:
            find_by_value_query = (
                f"""SELECT DISTINCT sub.name, sub.classes_per_semester, teach.name, teach.age
                    FROM subjects sub, teachers teach, subjects_teachers st
                    WHERE 
                        to_tsvector(sub.name) @@ plainto_tsquery('{subject_name}')
                        And st.subject_id = sub.id 
                        AND sub.classes_per_semester > {classes_range[0]}
                        AND sub.classes_per_semester < {classes_range[1]}
                        AND teach.age > {age_range[0]} 
                        AND teach.age < {age_range[1]}"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(find_by_value_query)
            for line in cursor.fetchall():
                print(line)
        except:
            print("Error: records were not found!")

    def find_schedule_records_by_id_name_day(self, id_range, teacher_name, day):
        try:
            find_by_value_query = (
                f"""SELECT DISTINCT sc.id, sc.day, sc.time, sub.name, teach.name, stud.name
                FROM scedule sc, subjects sub, teachers teach, students stud, subjects_teachers st
                WHERE
                    sc.id > {id_range[0]}
                    AND sc.id < {id_range[1]}
                    AND st.id = sc.subject_teacher_id 
                    AND sub.id = st.subject_id 
                    AND teach.id = st.teacher_id 
                    AND stud.id = sc.student_id 
                    AND to_tsvector(teach.name) 
                    @@ plainto_tsquery('{teacher_name}')
                    AND to_tsvector(sc.day) 
                    @@ plainto_tsquery('{day}')"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(find_by_value_query)
            for line in cursor.fetchall():
                print(line)
        except:
            print("Error: records were not found!")

    def find_marks_records_by_name_mark_grade(self, mark_range, grade, subject_name):
        try:
            find_by_value_query = (
                f"""SELECT DISTINCT ma.mark, stud.name, stud.grade, sub.name, teach.name
                    FROM subjects sub, teachers teach, subjects_teachers st, marks ma, students stud
                    WHERE 
                        ma.mark >= {mark_range[0]} 
                        AND ma.mark <= {mark_range[1]} 
                        AND stud.id = ma.student_id
                        AND st.id = ma.subject_teacher_id
                        AND teach.id = st.teacher_id   
                        AND stud.grade = {grade}
                        AND to_tsvector(sub.name) 
                        @@ plainto_tsquery('{subject_name}')"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(find_by_value_query)
            for line in cursor.fetchall():
                print(line)
        except:
            print("Error: records were not found!")

    # def __init__(self, connection, students, teachers, subjects, subjects_teachers, schedule, marks):
    #     self.connection = connection
    #     self.students = students
    #     self.teachers = teachers
    #     self.subjects = subjects
    #     self.subjects_teachers = subjects_teachers
    #     self.schedule = schedule
    #     self.marks = marks
    #
    # def find_subjects_teachers_records_by_name_classes_age(self, classes_range, subject_name, age_range):
    #     try:
    #         find_query = select([self.subjects.c.name,
    #                              self.subjects.classes_per_semester,
    #                              self.teachers.name,
    #                              self.teachers.age]).where(and_(
    #                                 self.subjects_teachers.c.subject_id == self.subjects.c.id,
    #                                 self.subjects.c.name == f'{subject_name}',
    #                                 self.subjects.c.classes_per_semester > {classes_range[0]},
    #                                 self.subjects.c.classes_per_semester < {classes_range[1]},
    #                                 self.teachers.c.age > {age_range[0]},
    #                                 self.teachers.c.age < {age_range[1]}))
    #
    #         result = self.connection.execute(find_query)
    #
    #         for line in result.fetchall():
    #             print(line)
    #     except:
    #         print("Error: records were not found!")
    #
    # def find_schedule_records_by_id_name_day(self, id_range, teacher_name, day):
    #     try:
    #         find_query = select([self.schedule.c.id,
    #                              self.schedule.c.day,
    #                              self.schedule.c.time,
    #                              self.subjects.c.name,
    #                              self.teachers.c.name,
    #                              self.students.c.name]).where(and_(
    #                                 self.schedule.c.id > id_range[0],
    #                                 self.schedule.c.id < id_range[1],
    #                                 self.subjects_teachers.id == self.schedule.c.subject_teacher_id,
    #                                 self.subjects.c.id == self.subjects_teachers.c.subject_id,
    #                                 self.teachers.c.id == self.subjects_teachers.c.teacher_id,
    #                                 self.students.c.id == self.schedule.c.student_id,
    #                                 self.teachers.c.name == f'{teacher_name}',
    #                                 self.schedule.c.day == f'{day}'))
    #
    #         result = self.connection.execute(find_query)
    #
    #         for line in result.fetchall():
    #             print(line)
    #     except:
    #         print("Error: records were not found!")
    #
    # def find_marks_records_by_name_mark_grade(self, mark_range, grade, subject_name):
    #     try:
    #         find_query = select([self.marks.c.points,
    #                              self.students.c.name,
    #                              self.students.c.grade,
    #                              self.subjects.c.name,
    #                              self.teachers.c.name]).where(and_(
    #                                 self.marks.c.points >= mark_range[0],
    #                                 self.marks.c.points <= mark_range[1],
    #                                 self.students.c.id == self.marks.c.student_id,
    #                                 self.subjects_teachers.c.id == self.marks.c.subject_teacher_id,
    #                                 self.teachers.c.id == self.subjects_teachers.c.teacher_id,
    #                                 self.students.c.grade == grade,
    #                                 self.subjects.c.name == f'{subject_name}'))
    #
    #         result = self.connection.execute(find_query)
    #
    #         for line in result.fetchall():
    #             print(line)
    #     except:
    #         print("Error: records were not found!")
