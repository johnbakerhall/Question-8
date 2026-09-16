# Group members: Cynthia Favour Kirabo, Wilson Mubbale, Kasujja John Baker,
# Apio Lewis Ruth, Ann Nakamatte, and Mugoya Arthur.
class Student:
    # Store the student's identity and current course enrollments.
    def __init__(self, reg_no, name):
        self.reg_no = reg_no
        self.name = name
        self.courses = []

    def __str__(self):
        return f"Student ID: {self.reg_no}\n Student name: {self.name}"

    def enrolled_courses(self):
        return self.courses



class Course:
    # Store course details and the students currently enrolled.
    def __init__(self, course_code, title, max_capacity):
        self.course_code = course_code
        self.title = title
        self.max_capacity = max_capacity
        self.enrolled_students = []

    def enroll_student(self, student):
        # Check if the student is already enrolled.
        if student in self.enrolled_students:
            print(f"Enrollment failed: Student {student.name} is already enrolled in {self.course_code}.")
            return False

        # Check if the course is full.
        if len(self.enrolled_students) >= self.max_capacity:
            print(f"Enrollment failed: Course {self.course_code} is full.")
            return False


        # Keep both sides of the student-course relationship in sync.
        # Add the student to the course
        self.enrolled_students.append(student)
        student.courses.append(self)
        print(f"Student {student.name} enrolled in {self.course_code}.")
        return True

    def drop_student(self, student):
        # Remove the student from both enrollment lists
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            student.courses.remove(self)
            print(f"Student {student.name} dropped from {self.course_code}.")
            return True
        else:
            print(f"Drop failed: Student {student.name} is not enrolled in {self.course_code}.")
            return False

    def available_places(self):
        return self.max_capacity - len(self.enrolled_students)

    def __str__(self):
        enrolled_names = ', '.join([student.name for student in self.enrolled_students])
        return (f"Course Code: {self.course_code}\n"
                f"Title: {self.title}\n"
                f"Capacity: {len(self.enrolled_students)}/{self.max_capacity}\n"
                f"Enrolled Students: {enrolled_names if enrolled_names else 'None'}")
# Group courses by department.
class Department:
    def __init__(self,dept_name, dept_code):
        self.dept_name = dept_name
        self.dept_code = dept_code
        self.courses = []   

    def __str__(self):
        return f"deptname: {self.dept_name} has the following courses  {self.courses}"
# Demonstrate the enrollment workflow.
if __name__ == "__main__":
    # Create sample students.
    student1 = Student("S001", "wilson")
    student2 = Student("S002", "baker")
    student3 = Student("S003", "john")

    # Create a course with room for two students.
    course1 = Course("CSE101", "Introduction to Data Science", 2)

    # Test successful, duplicate, and full-course enrollment.
    course1.enroll_student(student1)  # Should succeed
    course1.enroll_student(student1)  # Should fail (duplicate enrollment)
    course1.enroll_student(student2)  # Should succeed
    course1.enroll_student(student3)  # Should fail (course full)

    print(course1)

    # Dropping a student makes room for another enrollment.
    course1.drop_student(student1)  # Should succeed
    course1.enroll_student(student3)  # Should succeed now

    print(course1)
