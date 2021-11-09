import mvc_exceptions as mvc_exc

class Student:
    def __init__(self, connection):
        self.connection = connection


    def add_student(self, line):
        try:
            line_adding = line.split(", ")
            students = [(line_adding[0], line_adding[1], line_adding[2])]
            student_records = ", ".join(["%s"]*len(students))
            insert_query = (
                f"INSERT INTO students (name, age, grade) VALUES {student_records}"
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, students)
        except:
            print("Error: student was not added!")


    def update_student(self, line):
        try:
            line_editing = line.split(", ")
            update_student = f"""
            UPDATE
              students
            SET
              name = '{line_editing[1]}',
              age = '{line_editing[2]}',
              grade = '{line_editing[3]}'
            WHERE
              id = {line_editing[0]}
            """
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(update_student, line_editing)
        except:
            print("Error: student was not updated!")


    def delete_student(self, line_deleting):
        try:
            delete_student = f"DELETE FROM students WHERE id = '{line_deleting}'"
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(delete_student, line_deleting)
        except:
            print(f"Error: student with id = {line_deleting} does not exist!")


    def generate_random_students(self, line_adding):
        try:
            insert_query = (
                f"""INSERT INTO students(name, age, grade)
                SELECT
                chr(trunc(65+RANDOM()*25)::INT)||chr(trunc(65+RANDOM()*25)::INT) AS name,
                trunc(RANDOM() * 15 + 6)::INT AS age,
                trunc(RANDOM() * 10 + 2)::INT AS grade
                FROM GENERATE_SERIES(1, {line_adding}) seq;"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, line_adding)
        except:
            print("Error: student was not generated!")



class Teacher:
    def __init__(self, connection):
        self.connection = connection


    def add_teacher(self, line):
        try:
            line_adding = line.split(", ")
            teachers = [(line_adding[0], line_adding[1], line_adding[2])]
            teacher_records = ", ".join(["%s"] * len(teachers))
            insert_query = (
                f"INSERT INTO teachers (name, age, work_experience) VALUES {teacher_records}"
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, teachers)
        except:
            print("Error: teacher was not added!")

    def update_teacher(self, line):
        try:
            line_editing = line.split(", ")
            update_teacher = f"""
            UPDATE
              teachers
            SET
              name = '{line_editing[1]}',
              age = '{line_editing[2]}',
              work_experience = '{line_editing[3]}'
            WHERE
              id = {line_editing[0]}
            """
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(update_teacher, line_editing)
        except:
            print("Error: teacher was not updated!")

    def delete_teacher(self, line_deleting):
        try:
            delete_teacher = f"DELETE FROM teachers WHERE id = '{line_deleting}'"
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(delete_teacher, line_deleting)
        except:
            print(f"Error: teacher with id = {line_deleting} does not exist!")

    def generate_random_teachers(self, line_adding):
        try:
            insert_query = (
                f"""INSERT INTO teachers(name, age, work_experience)
                SELECT
                chr(trunc(65+RANDOM()*25)::INT)||chr(trunc(65+RANDOM()*25)::INT) AS name,
                trunc(RANDOM() * 10 + 6)::INT AS age,
                trunc(RANDOM() * 10 + 10)::INT AS work_experience
                FROM GENERATE_SERIES(1, {line_adding}) seq;"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, line_adding)
        except:
            print("Error: teacher was not generated!")




class Subject:
    def __init__(self, connection):
        self.connection = connection


    def add_subject(self, line):
        try:
            line_adding = line.split(", ")
            subjects = [(line_adding[0], line_adding[1])]
            subject_records = ", ".join(["%s"] * len(subjects))
            insert_query = (
                f"INSERT INTO teachers (name, classes_per_semester) VALUES {subject_records}"
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, subjects)
        except:
            print("Error: subject was not added!")

    def update_subject(self, line):
        try:
            line_editing = line.split(", ")
            update_subject = f"""
            UPDATE
              subjects
            SET
              name = '{line_editing[1]}',
              classes_per_semester = '{line_editing[2]}'
            WHERE
              id = {line_editing[0]}
            """
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(update_subject, line_editing)
        except:
            print("Error: subject was not updated!")

    def delete_subject(self, line_deleting):
        try:
            delete_subject = f"DELETE FROM subjects WHERE id = '{line_deleting}'"
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(delete_subject, line_deleting)
        except:
            print(f"Error: subject with id = {line_deleting} does not exist!")

    def generate_random_subjects(self, line_adding):
        try:
            insert_query = (
                f"""INSERT INTO subjects(name, classes_per_semester)
                SELECT
                chr(trunc(65+RANDOM()*25)::INT)||chr(trunc(65+RANDOM()*25)::INT) AS name,
                trunc(RANDOM() * 10 + 6)::INT AS classes_per_semester
                FROM GENERATE_SERIES(1, {line_adding}) seq;"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, line_adding)
        except:
            print("Error: subject was not generated!")



class Subject_Teacher:
    def __init__(self, connection):
        self.connection = connection


    def add_subjects_teachers_record(self, line):
        try:
            line_adding = line.split(", ")
            records = [(line_adding[0], line_adding[1])]
            subjects_teachers_records = ", ".join(["%s"] * len(records))
            insert_query = (
                f"INSERT INTO subjects_teachers (student_id, teacher_id) VALUES {subjects_teachers_records}"
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, records)
        except:
            print("Error: record was not added!")

    def update_subjects_teachers_record(self, line):
        try:
            line_editing = line.split(", ")
            update_record = f"""
            UPDATE
              subjects_teachers
            SET
              subject_id = '{line_editing[1]}',
              teacher_id = '{line_editing[2]}'
            WHERE
              id = {line_editing[0]}
            """
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(update_record, line_editing)
        except:
            print("Error: record was not updated!")

    def delete_subjects_teachers_record(self, line_deleting):
        try:
            delete_record = f"DELETE FROM subjects_teachers WHERE id = '{line_deleting}'"
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(delete_record, line_deleting)
        except:
            print(f"Error: record with id = {line_deleting} does not exist!")

    def generate_random_subjects_teachers_records(self, line_adding):
        try:
            insert_query = (
                f"""INSERT INTO subjects_teachers(subject_id, teacher_id)
                SELECT
                trunc(RANDOM() * 10 + 6)::INT AS subject_id,
                trunc(RANDOM() * 10 + 3)::INT AS teacher_id
                FROM GENERATE_SERIES(1, {line_adding}) seq;"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, line_adding)
        except:
            print("Error: record was not generated!")




class Schedule:
    def __init__(self, connection):
        self.connection = connection


    def add_schedule_record(self, line):
        try:
            line_adding = line.split(", ")
            record = [(line_adding[0], line_adding[1], line_adding[2], line_adding[3])]
            schedule_records = ", ".join(["%s"] * len(record))
            insert_query = (
                f"INSERT INTO scedule (day, time, subject_teacher_id, student_id) VALUES {schedule_records}"
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, record)
        except:
            print("Error: record was not added!")

    def update_schedule_record(self, line):
        try:
            line_editing = line.split(", ")
            update_record = f"""
            UPDATE
              scedule
            SET
              day = '{line_editing[1]}',
              time = '{line_editing[2]}',
              subject_teacher_id = '{line_editing[3]}',
              student_id = '{line_editing[4]}'
            WHERE
              id = {line_editing[0]}
            """
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(update_record, line_editing)
        except:
            print("Error: record was not updated!")

    def delete_schedule_record(self, line_deleting):
        try:
            delete_record = f"DELETE FROM scedule WHERE id = '{line_deleting}'"
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(delete_record, line_deleting)
        except:
            print(f"Error: record with id = {line_deleting} does not exist!")

    def generate_random_schedule_records(self, line_adding):
        try:
            insert_query = (
                f"""INSERT INTO scedule(day, time, subject_teacher_id, student_id)
                SELECT
                CASE trunc(RANDOM() * 10)::INT
                 WHEN 0 THEN 'monday'
                 WHEN 1 THEN 'tuesday'
                 WHEN 2 THEN 'wednesday'
                 WHEN 3 THEN 'thursday'
                 WHEN 4 THEN 'friday'
                 ELSE 'saturday'
                END AS day,
                trunc(RANDOM() * 10 + 5)::INT||':'||trunc(RANDOM() * 10 + 5)::INT AS time,
                trunc(RANDOM() * 2 + 1)::INT AS subject_teacher_id,
                trunc(RANDOM() * 2 + 1)::INT AS student_id
                FROM GENERATE_SERIES(1, {line_adding}) seq;"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, line_adding)
        except:
            print("Error: record was not generated!")




class Mark:
    def __init__(self, connection):
        self.connection = connection

    def add_mark(self, line):
        try:
            line_adding = line.split(", ")
            marks = [(line_adding[0], line_adding[1], line_adding[2])]
            mark_records = ", ".join(["%s"] * len(marks))
            insert_query = (
                f"INSERT INTO marks (student_id, subject_teacher_id, mark) VALUES {mark_records}"
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, marks)
        except:
            print("Error: mark was not added!")

    def update_mark(self, line):
        try:
            line_editing = line.split(", ")
            update_mark = f"""
               UPDATE
                 marks
               SET
                 name = '{line_editing[1]}',
                 subject_teacher_id = '{line_editing[2]}',
                 mark = '{line_editing[3]}'
               WHERE
                 id = {line_editing[0]}
               """
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(update_mark, line_editing)
        except:
            print("Error: mark was not updated!")

    def delete_mark(self, line_deleting):
        try:
            delete_mark = f"DELETE FROM marks WHERE id = '{line_deleting}'"
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(delete_mark, line_deleting)
        except:
            print(f"Error: mark with id = {line_deleting} does not exist!")

    def generate_random_marks(self, line_adding):
        try:
            insert_query = (
                f"""INSERT INTO marks(student_id, subject_teacher_id, mark)
                SELECT
                trunc(RANDOM() * 2 + 1)::INT AS student_id,
                trunc(RANDOM() * 2 + 1)::INT AS subject_teacher_id,
                trunc(RANDOM() * 10 + 5)::INT AS mark
                FROM GENERATE_SERIES(1, {line_adding}) seq;"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(insert_query, line_adding)
        except:
            print("Error: mark was not generated!")




class Search:
    def __init__(self, connection):
        self.connection = connection


    def find_subjects_teachers_records_by_name_classes_age(self, classes_range, subject_name, age_range):
        try:
            find_by_value_query = (
                f"""SELECT DISTINCT sub.name, sub.classes_per_semester, teach.name, teach.age
                    FROM subjects sub, teachers teach, subjects_teachers st
                    WHERE 
                        st.subject_id = sub.id 
                        AND sub.name = '{subject_name}' 
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
                    AND teach.name LIKE '%{teacher_name}%'
                    AND sc.day = '{day}'"""
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
                        AND stud.grade = '{grade}'
                        AND sub.name LIKE '%{subject_name}%'"""
            )
            self.connection.autocommit = True
            cursor = self.connection.cursor()
            cursor.execute(find_by_value_query)
            for line in cursor.fetchall():
                print(line)
        except:
            print("Error: records were not found!")
