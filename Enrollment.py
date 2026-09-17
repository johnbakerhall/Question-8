
#Group Project - Topic 5: Scalable OOP System
#Group 8 - Course Enrolment System
#Group Members: FAVOUR CYNTHIA KIRABO-M25B38/018, 

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            print(f"{self.name} has been enrolled in {course}.")
        else:
            print(f"{self.name} is already enrolled in {course}.")

    def drop(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print(f"{self.name} has dropped {course}.")
        else:
            print(f"{self.name} is not enrolled in {course}.")

    def list_courses(self):
        if self.courses:
            print(f"{self.name} is enrolled in the following courses: {', '.join(self.courses)}")
        else:
            print(f"{self.name} is not enrolled in any courses.")
