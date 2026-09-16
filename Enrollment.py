<<<<<<< HEAD

class Student:
    # A student is identified by a registration number and name.
    # Each student keeps track of the courses they are enrolled in.
=======
# Group members: Cynthia Favour Kirabo, Wilson Mubbale, Kasujja John Baker,
# Apio Lewis Ruth, Ann Nakamatte, and Mugoya Arthur.
class Student:
    # Store the student's identity and current course enrollments.
>>>>>>> 9f836ae979b9bc8c55356b11aa066860d7ba1c2e
    def __init__(self, reg_no, name):
        self.reg_no = reg_no
        self.name = name
        self.courses = []

    def __str__(self):
<<<<<<< HEAD
        # Display the student's identity in a readable format.
        return f"Student ID: {self.reg_no}\n Student name: {self.name}"

    def enrolleled_courses(self):
        for course in self.courses:
            print(f"{course.course_code}: {course.title}")  
        # Return the list of courses the student is currently taking.
        return self.courses


class Course:
    # A course has a code, title, capacity, and a list of enrolled students.
=======
        return f"Student ID: {self.reg_no}\n Student name: {self.name}"

    def enrolled_courses(self):
        return self.courses



class Course:
    # Store course details and the students currently enrolled.
>>>>>>> 9f836ae979b9bc8c55356b11aa066860d7ba1c2e
    def __init__(self, course_code, title, max_capacity):
        self.course_code = course_code
        self.title = title
        self.max_capacity = max_capacity
        self.enrolled_students = []

    def enroll_student(self, student):
<<<<<<< HEAD
        # Refuse enrollment if the student is already in the class.
=======
        # Check if the student is already enrolled.
>>>>>>> 9f836ae979b9bc8c55356b11aa066860d7ba1c2e
        if student in self.enrolled_students:
            print(f"Enrollment failed: Student {student.name} is already enrolled in {self.course_code}.")
            return False

<<<<<<< HEAD
        # Refuse enrollment if the course is already full.
=======
        # Check if the course is full.
>>>>>>> 9f836ae979b9bc8c55356b11aa066860d7ba1c2e
        if len(self.enrolled_students) >= self.max_capacity:
            print(f"Enrollment failed: Course {self.course_code} is full.")
            return False


<<<<<<< HEAD
        # Refuse enrollment if the student is already in the class.
        if student in self.enrolled_students:
            print(f"Enrollment failed: Student {student.name} is already enrolled in {self.course_code}.")
            return False

        # Add the student to the course and record the course for the student.
        self.enrolled_students.append(student)
        student.courses.append(self)
=======
        # Keep both sides of the student-course relationship in sync.
        
        # Add the student to the course
        self.enrolled_students.append(student)

        # Add the course to the student's course list. 
        student.courses.append(self)
        
>>>>>>> 9f836ae979b9bc8c55356b11aa066860d7ba1c2e
        print(f"Student {student.name} enrolled in {self.course_code}.")
        return True

    def drop_student(self, student):
<<<<<<< HEAD
        # Remove the student only if they are currently enrolled.
=======
        # Remove the student from both enrollment lists
>>>>>>> 9f836ae979b9bc8c55356b11aa066860d7ba1c2e
        if student in self.enrolled_students:
            self.enrolled_students.remove(student)
            student.courses.remove(self)
            print(f"Student {student.name} dropped from {self.course_code}.")
            return True
        else:
            print(f"Drop failed: Student {student.name} is not enrolled in {self.course_code}.")
            return False

    def available_places(self):
<<<<<<< HEAD
        # Calculate how many places are still open in the course.
        return self.max_capacity - len(self.enrolled_students)

    def __str__(self):
        # Build a readable summary of the course and its students.
=======
        return self.max_capacity - len(self.enrolled_students)

    def __str__(self):
>>>>>>> 9f836ae979b9bc8c55356b11aa066860d7ba1c2e
        enrolled_names = ', '.join([student.name for student in self.enrolled_students])
        return (f"Course Code: {self.course_code}\n"
                f"Title: {self.title}\n"
                f"Capacity: {len(self.enrolled_students)}/{self.max_capacity}\n"
                f"Enrolled Students: {enrolled_names if enrolled_names else 'None'}")
<<<<<<< HEAD
#adding a department class to the code
class Department:
=======
# Group courses by department.
class Department:
    # A department has a name, code and list of courses.
>>>>>>> 9f836ae979b9bc8c55356b11aa066860d7ba1c2e
    def __init__(self,dept_name, dept_code):
        self.dept_name = dept_name
        self.dept_code = dept_code
        self.courses = []   
<<<<<<< HEAD

    def __str__(self):
        return f"deptname: {self.dept_name} has the following courses  {self.courses}"
# Example usage of the classes
if __name__ == "__main__":
    # Create some students
    student1 = Student("S001", "wilson")
    student2 = Student("S002", "baker")
    student3 = Student("S003", "john")

    # Create a course with a capacity of 2
    course1 = Course("CSE101", "Introduction to Computer Science", 2)

    # Enroll students in the course
    course1.enroll_student(student1)  # Should succeed
    course1.enroll_student(student2)  # Should succeed
    course1.enroll_student(student3)  # Should fail (course full)

    # Print course details
    print(course1)

    # Drop a student and try enrolling again
    course1.drop_student(student1)  # Should succeed
    course1.enroll_student(student3)  # Should succeed now

    # Print updated course details
    print(course1)
=======
        
    def __str__(self):
        return f"deptname: {self.dept_name} has the following courses  {self.courses}"
# Demonstrate the enrollment workflow.
if __name__ == "__main__":
    # Create sample students.
    student1 = Student("S001", "wilson")
    student2 = Student("S002", "baker")
    student3 = Student("S003", "ruth")

    # Create a course with room for two students.
    course1 = Course("BSDS101", "Introduction to Data Science", 2)

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
>>>>>>> 9f836ae979b9bc8c55356b11aa066860d7ba1c2e
