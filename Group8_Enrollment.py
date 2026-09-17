''' Group members:

 1- Favour Cynthia KIrabo
 2- Wilson Mubbale
 3- Kasujja John Baker
 4- Apio Lewis Ruth
 5- Ann Nakamatte
 6- Mugoya Arthur
 
 '''
# A student is identified by the registration number and name.
    #Each student keeps track of the courses they are enrolled in.
    #Store the student's identity and current course enrollments.
class Student:    
    def __init__(self, reg_no, name):
        self.reg_no = reg_no
        self.name = name
        self.courses = [] #where the sudents courses will be stored

    def __str__(self):
        # Helps to display the student's identity in a readable format.
        return f"Student ID: {self.reg_no}\n Student name: {self.name}"

    def enrolled_courses(self):
        # Return the list of courses the student is taking currently.
        for course in self.courses:
            print(f"{course.course_code}: {course.title}")  


class Course:
    #A course has a code, title, capacity, and a list of enrolled students.
    #Store course details and the students currently enrolled.
    def __init__(self, course_code, title, max_capacity):
        self.course_code = course_code
        self.title = title
        self.max_capacity = max_capacity
        self.enrolled_students = []

    def enroll_student(self, student):
        #Refuse enrollment if the student is already in the class.
        #Check if the student is already enrolled.
        if student in self.enrolled_students:
            print(f"Enrollment failed: Student {student.name} is already enrolled in {self.course_code}.")
            return False

        #Refuse enrollment if the course is already full.
        #Check if the course is full.
        if self.available_places() <= 0:
            print(f"Enrollment failed: Course {self.course_code} is full.")
            return False

        #Keep both sides of the student-course relationship in sync.
        #Add the student to the course.
        self.enrolled_students.append(student)
        # Add the course to the student's course list.
        student.courses.append(self)
        print(f"Student {student.name} enrolled in {self.course_code}.")
        return True

    def drop_student(self, student):
        #Remove the student only if they are currently enrolled.
        #Remove the student from both enrollment lists.
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            student.courses.remove(self)
            print(f"Student {student.name} dropped from {self.course_code}.")
            return True
        else:
            print(f"Drop failed: Student {student.name} is not enrolled in {self.course_code}.")
            return False

    def available_places(self):
        #Calculate how many places are still open in the course.
        return self.max_capacity - len(self.enrolled_students)

    def __str__(self):
        # Build a readable summary of the course and its students.
        enrolled_names = ', '.join([student.name for student in self.enrolled_students])
        return (f"Course Code: {self.course_code}\n"
                f"Title: {self.title}\n"
                f"Capacity: {len(self.enrolled_students)}/{self.max_capacity}\n"
                f"Enrolled Students: {enrolled_names if enrolled_names else 'None'}")
#Adding a department class to the code.
#Group courses by department.
class Department:
    #A department has a name, code and list of courses.
    def __init__(self,dept_name, dept_code):
        self.dept_name = dept_name
        self.dept_code = dept_code
        self.courses = [] 


    def add_course(self, course):
        #Add a course to the department's list of courses.
        if course not in self.courses:
            self.courses.append(course)
            print(f"Course {course.course_code} added to department {self.dept_name}.")
            return True
        else:
            print(f"Course {course.course_code} is already in department {self.dept_name}.")
            return False

    def __str__(self):
        return f"deptname: {self.dept_name} has the following courses  {self.courses}"
# Example usage of the classes.
# Demonstrate the enrollment workflow from user input


if __name__ == "__main__":

    print("===== STUDENT COURSE ENROLLMENT SYSTEM =====")

    # Get student information from the user
    students = []

    number_of_students = int(input("Enter number of students: "))

    for i in range(number_of_students):
        print(f"\nEnter details for Student {i + 1}")
        reg_no = input("Registration number: ")
        name = input("Student name: ")

        student = Student(reg_no, name)
        students.append(student)

    # Get course information from the user
    courses = []

    number_of_courses = int(input("\nEnter number of courses: "))

    for i in range(number_of_courses):
        print(f"\nEnter details for Course {i + 1}")
        course_code = input("Course code: ")
        title = input("Course title: ")
        max_capacity = int(input("Maximum capacity: "))

        course = Course(course_code, title, max_capacity)
        courses.append(course)

    # Create a department
    print("\n===== DEPARTMENT DETAILS =====")
    dept_name = input("Enter department name: ")
    dept_code = input("Enter department code: ")

    department = Department(dept_name, dept_code)

    # Add all courses to the department
    for course in courses:
        department.add_course(course)

    # Enrollment menu
    while True:
        print("\n===== ENROLLMENT MENU =====")
        print("1. Enroll student")
        print("2. Drop student")
        print("3. View course details")
        print("4. View student's courses")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nAvailable Students:")

            for i, student in enumerate(students):
                print(f"{i + 1}. {student.reg_no} - {student.name}")

            student_choice = int(input("Select student: "))

            print("\nAvailable Courses:")

            for i, course in enumerate(courses):
                print(
                    f"{i + 1}. {course.course_code} - "
                    f"{course.title} "
                    f"({course.available_places()} places available)"
                )

            course_choice = int(input("Select course: "))

            student = students[student_choice - 1]
            course = courses[course_choice - 1]

            course.enroll_student(student)

        elif choice == "2":
            print("\nStudents:")

            for i, student in enumerate(students):
                print(f"{i + 1}. {student.reg_no} - {student.name}")

            student_choice = int(input("Select student: "))

            print("\nCourses:")

            for i, course in enumerate(courses):
                print(f"{i + 1}. {course.course_code} - {course.title}")

            course_choice = int(input("Select course: "))

            student = students[student_choice - 1]
            course = courses[course_choice - 1]

            course.drop_student(student)

        elif choice == "3":
            print("\nCourses:")

            for i, course in enumerate(courses):
                print(f"{i + 1}. {course.course_code} - {course.title}")

            course_choice = int(input("Select course: "))

            course = courses[course_choice - 1]

            print("\n===== COURSE DETAILS =====")
            print(course)

        elif choice == "4":
            print("\nStudents:")

            for i, student in enumerate(students):
                print(f"{i + 1}. {student.reg_no} - {student.name}")

            student_choice = int(input("Select student: "))

            student = students[student_choice - 1]

            print(f"\nCourses enrolled by {student.name}:")
            student.enrolled_courses()

            if not student.courses:
                print("No courses enrolled.")

        elif choice == "5":
            print("Thank you for using the Student Course Enrollment System.")
            break

        else:
            print("Invalid choice. Please try again.")