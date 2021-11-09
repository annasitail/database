import psycopg2
from psycopg2 import OperationalError
from view import View
from model import Student, Teacher, Subject, Subject_Teacher, Schedule, Mark, Search



def create_connection():
    connection = None
    try:
        connection = psycopg2.connect(
            database='postgres',
            user='postgres',
            password=1234567890,
            host='localhost',
            port=5432,
        )
    except OperationalError as e:
        print(f"The error '{e}' occurred")
    return connection

def run(command):
    connection = create_connection()

    student = Student(connection)
    teacher = Teacher(connection)
    subject = Subject(connection)
    subject_teacher = Subject_Teacher(connection)
    schedule = Schedule(connection)
    mark = Mark(connection)
    search = Search(connection)

    view = View()

    if command == "add student":
        try:
            command_line = view.ask_for_values_to_add("student")
            v1 = command_line.split(", ")[0]
            v2 = int(command_line.split(", ")[1])
            v3 = int(command_line.split(", ")[2])
            student.add_student(command_line)
            view.added_message("student")
        except:
            view.incorrect_input_message("student")
    elif command == "update student":
        try:
            command_line = view.ask_for_values_to_update("student")
            v1 = command_line.split(", ")[0]
            v2 = int(command_line.split(", ")[1])
            v3 = int(command_line.split(", ")[2])
            student.update_student(command_line)
            view.updated_message("student")
        except:
            view.incorrect_input_message("student")
    elif command == "delete student":
        try:
            command_line = int(view.ask_for_values_to_delete("student"))
            student.delete_student(command_line)
            view.deleted_message("student")
        except:
            view.incorrect_input_message("student")
    elif command == "get random students":
        try:
            command_line = int(view.ask_for_values_to_generate("student"))
            student.generate_random_students(command_line)
            view.generated_message("student")
        except:
            view.incorrect_input_message("student")
    elif command == "add teacher":
        try:
            command_line = view.ask_for_values_to_add("teacher")
            v1 = command_line.split(", ")[0]
            v2 = int(command_line.split(", ")[1])
            v3 = int(command_line.split(", ")[2])
            teacher.add_teacher(command_line)
            view.added_message("teacher")
        except:
            view.incorrect_input_message("teacher")
    elif command == "update teacher":
        try:
            command_line = view.ask_for_values_to_update("teacher")
            v1 = command_line.split(", ")[0]
            v2 = int(command_line.split(", ")[1])
            v3 = int(command_line.split(", ")[2])
            teacher.update_teacher(command_line)
            view.updated_message("teacher")
        except:
            view.incorrect_input_message("teacher")
    elif command == "delete teacher":
        try:
            command_line = int(view.ask_for_values_to_delete("teacher"))
            teacher.delete_teacher(command_line)
            view.deleted_message("teacher")
        except:
            view.incorrect_input_message("teacher")
    elif command == "get random teachers":
        try:
            command_line = int(view.ask_for_values_to_generate("teacher"))
            teacher.generate_random_teachers(command_line)
            view.generated_message("teacher")
        except:
            view.incorrect_input_message("teacher")
    elif command == "add subject":
        try:
            command_line = view.ask_for_values_to_add("subject")
            v1 = command_line.split(", ")[0]
            v2 = int(command_line.split(", ")[1])
            subject.add_subject(command_line)
            view.added_message("subject")
        except:
            view.incorrect_input_message("subject")
    elif command == "update subject":
        try:
            command_line = view.ask_for_values_to_update("subject")
            v1 = command_line.split(", ")[0]
            v2 = int(command_line.split(", ")[1])
            subject.update_subject(command_line)
            view.updated_message("subject")
        except:
            view.incorrect_input_message("subject")
    elif command == "delete subject":
        try:
            command_line = view.ask_for_values_to_delete("subject")
            v = int(command_line)
            subject.delete_subject(command_line)
            view.deleted_message("subject")
        except:
            view.incorrect_input_message("subject")
    elif command == "get random subjects":
        try:
            command_line = view.ask_for_values_to_generate("subject")
            v = int(command_line)
            subject.generate_random_subjects(command_line)
            view.generated_message("subject")
        except:
            view.incorrect_input_message("subject")
    elif command == "add subjects_teachers record":
        try:
            command_line = view.ask_for_values_to_add("subjects_teachers record")
            v1 = int(command_line.split(", ")[0])
            v2 = int(command_line.split(", ")[1])
            subject_teacher.add_subjects_teachers_record(command_line)
            view.added_message("subjects_teachers record")
        except:
            view.incorrect_input_message("subjects_teachers record")
    elif command == "update subjects_teachers record":
        try:
            command_line = view.ask_for_values_to_update("subjects_teachers record")
            v1 = int(command_line.split(", ")[0])
            v2 = int(command_line.split(", ")[1])
            subject_teacher.update_subjects_teachers_record(command_line)
            view.updated_message("subjects_teachers record")
        except:
            view.incorrect_input_message("subjects_teachers record")
    elif command == "delete subjects_teachers record":
        try:
            command_line = view.ask_for_values_to_delete("subjects_teachers record")
            v = int(command_line)
            subject_teacher.delete_subjects_teachers_record(command_line)
            view.deleted_message("subjects_teachers record")
        except:
            view.incorrect_input_message("subjects_teachers record")
    elif command == "get random subjects_teachers records":
        try:
            command_line = view.ask_for_values_to_generate("subjects_teachers record")
            v = int(command_line)
            subject_teacher.generate_random_subjects_teachers_records(command_line)
            view.generated_message("subjects_teachers record")
        except:
            view.incorrect_input_message("subjects_teachers record")
    elif command == "add schedule record":
        try:
            command_line = view.ask_for_values_to_add("schedule")
            v1 = command_line.split(", ")[0]
            v2 = command_line.split(", ")[1]
            v3 = int(command_line.split(", ")[2])
            v4 = int(command_line.split(", ")[3])
            schedule.add_schedule_record(command_line)
            view.added_message("schedule")
        except:
            view.incorrect_input_message("schedule")
    elif command == "update schedule record":
        try:
            command_line = view.ask_for_values_to_update("schedule")
            v1 = command_line.split(", ")[0]
            v2 = command_line.split(", ")[1]
            v3 = int(command_line.split(", ")[2])
            v4 = int(command_line.split(", ")[3])
            schedule.update_schedule_record(command_line)
            view.updated_message("schedule")
        except:
            view.incorrect_input_message("schedule")
    elif command == "delete schedule record":
        try:
            command_line = view.ask_for_values_to_delete("schedule")
            v = int(command_line)
            schedule.delete_schedule_record(command_line)
            view.deleted_message("schedule")
        except:
            view.incorrect_input_message("schedule")
    elif command == "get random schedule records":
        try:
            command_line = view.ask_for_values_to_generate("schedule")
            v = int(command_line)
            schedule.generate_random_schedule_records(command_line)
            view.generated_message("schedule")
        except:
            view.incorrect_input_message("schedule")
    elif command == "add mark record":
        try:
            command_line = view.ask_for_values_to_add("mark record")
            v1 = int(command_line.split(", ")[0])
            v2 = int(command_line.split(", ")[1])
            v3 = int(command_line.split(", ")[2])
            mark.add_mark(command_line)
            view.added_message("mark record")
        except:
            view.incorrect_input_message("mark record")
    elif command == "update mark record":
        try:
            command_line = view.ask_for_values_to_update("mark record")
            v1 = int(command_line.split(", ")[0])
            v2 = int(command_line.split(", ")[1])
            v3 = int(command_line.split(", ")[2])
            mark.update_mark(command_line)
            view.updated_message("mark record")
        except:
            view.incorrect_input_message("mark record")
    elif command == "delete mark record":
        try:
            command_line = view.ask_for_values_to_delete("mark record")
            v = int(command_line)
            mark.delete_mark(command_line)
            view.deleted_message("mark record")
        except:
            view.incorrect_input_message("mark record")
    elif command == "get random mark records":
        try:
            command_line = view.ask_for_values_to_generate("mark record")
            v = int(command_line)
            mark.generate_random_marks(command_line)
            view.generated_message("mark record")
        except:
            view.incorrect_input_message("mark record")
    elif command == "search subjects_teachers records by name, classes, age":
        try:
            classes_range = view.ask_for_values_to_search("classes per semester range").split(", ")
            subject_name = view.ask_for_values_to_search("subject name")
            age_range = view.ask_for_values_to_search("teacher age range").split(", ")
            v1 = int(classes_range[0])
            v2 = int(classes_range[1])
            v3 = subject_name
            v4 = int(age_range[0])
            v5 = int(age_range[1])
            view.before_and_after_search("started")
            search.find_subjects_teachers_records_by_name_classes_age(classes_range, subject_name, age_range)
            view.before_and_after_search("ended")
        except:
            view.incorrect_input_message("search")
    elif command == "search schedule records by id, name, day":
        try:
            id_range = view.ask_for_values_to_search("id range").split(", ")
            teacher_name = view.ask_for_values_to_search("teacher's name")
            day = view.ask_for_values_to_search("day")
            v1 = int(id_range[0])
            v2 = int(id_range[1])
            v3 = teacher_name
            v4 = day
            view.before_and_after_search("started")
            search.find_schedule_records_by_id_name_day(id_range, teacher_name, day)
            view.before_and_after_search("ended")
        except:
            view.incorrect_input_message("search")
    elif command == "search marks records by name, mark, grade":
        try:
            mark_range = view.ask_for_values_to_search("mark range").split(", ")
            subject_name = view.ask_for_values_to_search("subject name")
            grade = view.ask_for_values_to_search("grade")
            v1 = int(mark_range[0])
            v2 = int(mark_range[1])
            v3 = subject_name
            v4 = int(grade)
            view.before_and_after_search("started")
            search.find_marks_records_by_name_mark_grade(mark_range, grade, subject_name)
            view.before_and_after_search("ended")
        except:
            view.incorrect_input_message("search")
    else:
        print("Unknown command, try again!")