class Student:
    def __init__(self):                                     #constructor
        self.__id = input("Enter student's ID: ")       #this.ctct
        self.__name = input("Enter student's name: ")   
        self.__dob = input("Enter student's dob: ")

    def get_id(self):                                       #getter
        return self.__id

    def get_name(self):
        return self.__name

    def get_dob(self):
        return self.__dob

class Course:
    def __init__(self):
        self.__id = input("Enter course ID: ")
        self.__name = input("Enter course's name: ")

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

class Mark:
    def __init__(self):
        self.__marks = {}       #blank dictionary

    def add_mark(self, student_id, course_id, mark):
        if student_id not in self.__marks:
            self.__marks[student_id] = {}
        self.__marks[student_id][course_id] = mark

    def get_mark(self, student_id, course_id):
        return self.__marks.get(student_id, {}).get(course_id, "NULL")

class Utils:
    @staticmethod                                       #method ko có self trong parameter --> nhập gtri từ ngoài
    def input_data(args):
        return int(input(f"Enter the number of {args}: "))  #f để {args} in ra giá trị đc input

    @staticmethod
    def show(list, label):
        print(f"{label} list:")
        for i, item in enumerate(list, start=1):
            print(f"{i}. {item.get_id()} - {item.get_name()}")

class University:
    def __init__(self):
        self.__num_students = 0
        self.__num_courses = 0
        self.__students = []
        self.__courses = []
        self.__marks = Mark()

    def get_num_students(self):
        return self.__num_students

    def get_num_courses(self):
        return self.__num_courses

    def get_students(self):
        return self.__students

    def get_courses(self):
        return self.__courses

    def set_num_students(self):
        self.__num_students = Utils.input_data("students")

    def set_num_courses(self):
        self.__num_courses = Utils.input_data("courses")

    def set_students(self):
        for _ in range(self.get_num_students()):
            student = Student()
            self.__students.append(student)

    def set_courses(self):
        for _ in range(self.get_num_courses()):
            course = Course()
            self.__courses.append(course)

    def list_students(self):
        Utils.show(self.get_students(), "Student")

    def list_courses(self):
        Utils.show(self.get_courses(), "Course")

    def input_student_mark(self):
        self.list_courses()
        course_id = input("Input course ID to mark: ")
        if any(course_id == course.get_id() for course in self.get_courses()):
            student_id = input("Input student ID to mark: ")
            if any(student_id == student.get_id() for student in self.get_students()):
                mark = int(input("Enter mark: "))
                self.__marks.add_mark(student_id, course_id, mark)
                print("Mark successfully")
            else:
                print(f"Student ID {student_id} not exist")
        else:
            print(f"Course {course_id} not exist")

    def show_student_mark(self):
        for course in self.get_courses():
            course_id = course.get_id()
            print(f"Mark of Course: {course.get_name()} - {course_id}:")
            print("No - Student Name - Student ID - Date of Birth - Mark")
            for i, student in enumerate(self.get_students(), start=1):
                student_id = student.get_id()
                mark = self.__marks.get_mark(student_id, course_id)
                print(f"{i}. {student.get_name()} - {student_id} - {student.get_dob()} - {mark}")
            print("")


def main():
    university = University()

    while True: #lặp mãi mãi ko ĐK
        print("""
    0. Exit
    1. Set number of students
    2. Set number of courses
    3. Set students
    4. Set courses
    5. List all students
    6. List all courses
    7. Input student's mark
    8. Show student's mark
        """)
        option = int(input("Your choice: "))
        if option == 0:
            break
        elif option == 1:
            university.set_num_students()
        elif option == 2:
            university.set_num_courses()
        elif option == 3:
            university.set_students()
        elif option == 4:
            university.set_courses()
        elif option == 5:
            university.list_students()
        elif option == 6:
            university.list_courses()
        elif option == 7:
            university.input_student_mark()
        elif option == 8:
            university.show_student_mark()
        else:
            print("Invalid input. Please try again!")

if __name__ == "__main__":
    main()