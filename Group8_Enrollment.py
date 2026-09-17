''' Group members:

 1- Cynthia Favour Kirabo
 2- Wilson Mubbale
 3- Kasujja John Baker
 4- Apio Lewis Ruth
 5- Ann Nakamatte
 6- Mugoya Arthur
 
 '''
# A student is identified by a registration number and name.
    #Each student keeps track of the courses they are enrolled in.
    #Store the student's identity and current course enrollments.
class Student:    
    def __init__(self, reg_no, name):
        self.reg_no = reg_no
        self.name = name
        self.courses = []

    def __str__(self):
        # Display the student's identity in a readable format.
        return f"Student ID: {self.reg_no}\n Student name: {self.name}"

    def enrolled_courses(self):
        # Return the list of courses the student is currently taking.
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
# Adding a department class to the code.
# Group courses by department.
class Department:
    # A department has a name, code and list of courses.
    def __init__(self,dept_name, dept_code):
        self.dept_name = dept_name
        self.dept_code = dept_code
        self.courses = [] 


    def add_course(self, course):
        # Add a course to the department's list of courses.
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
    # Create some students.
    student1 = Student("S001", "wilson")
    student2 = Student("S002", "baker")
    student3 = Student("S003", "john")

    # Create a course with a capacity of 2.
    course1 = Course("CSE101", "Introduction to Computer Science", 2)
    course2 = Course("CSE102", "Data Structures", 3)
    Department1 = Department("Engineering Department", "ES")
    Department1.add_course(course1)
    Department1.add_course(course2)

    # Enroll students in the course.
    course1.enroll_student(student1)  # Should succeed.
    course1.enroll_student(student2)  # Should succeed.
    course1.enroll_student(student3)  # Should fail (course full).

    # Print course details.
    print(course1)

    # Drop a student and try enrolling again.
    course1.drop_student(student1)  # Should succeed.
    course1.enroll_student(student3)  # Should succeed now.

    # Print updated course details.
    print(course1)
