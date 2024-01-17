num_students = int(input("Enter the number of students in the class: "))
students =[]

for _ in range(num_students):
    id = input("Enter student ID: ")
    name = input("Enter student name: ")
    dob = input("Enter student date of birth (DoB): ")
    students.append((id, name, dob, {})) 

num_courses = int(input("Enter the number of courses: "))
courses = []


for _ in range(num_courses):
    id = input("Enter course ID: ")
    name = input("Enter course name: ")
    courses.append((id, name)) 

def input_marks(student, course, marks):
    for s in students:
        if s[0] == student:
            s[3][course] = marks 

def list_courses():
    print("List of courses:")
    for course in courses:
        print(f"ID: {course[0]}, Name: {course[1]}")

def list_students():
    print("List of students:")
    for student in students:
        print(f"ID: {student[0]}, Name: {student[1]}, DoB: {student[2]}")

def show_student_marks(student_id, course_id):
    for student in students:
        if student[0] == student_id:
            marks = student[3].get(course_id, "N/A")
            print(f"Student {student[1]} scored {marks} in course {course_id}")
