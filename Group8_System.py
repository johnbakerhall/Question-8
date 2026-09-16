"""
CSC2105: Object-Oriented Programming Using Python
Group Project - Scalable OOP System (Topic 5 foundation)

GROUP 8 - Course Enrolment System

Group members:
    - [Name 1]
    - [Name 2]
    - [Name 3]
    - [Name 4]

Scenario:
A department runs courses that only have a limited number of places.
Each course has a code, a title, a maximum capacity, and a list of
enrolled students. Students may enrol or leave a course. Enrolment is
refused if the course is full or the student is already enrolled, and
the system explains why in both cases.
"""


class EnrollmentError(Exception):
    """Raised when a student cannot be enrolled on, or dropped from, a course."""
    pass


class Student:
    """A student who can be enrolled on courses."""

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def __eq__(self, other):
        # Two students are considered the same person if their names match.
        # (Good enough for this stage; a student ID could replace this later.)
        if isinstance(other, Student):
            return self.name.strip().lower() == other.name.strip().lower()
        return False

    def __hash__(self):
        return hash(self.name.strip().lower())


class Course:
    """A course with a limited number of places."""

    def __init__(self, code, title, capacity):
        self.code = code
        self.title = title
        self.capacity = capacity
        self._enrolled = []  # list of Student objects currently on the course

    def is_full(self):
        """Return True if the course has no places left."""
        return len(self._enrolled) >= self.capacity

    def is_enrolled(self, student):
        """Return True if this student is already on the course."""
        return student in self._enrolled

    def places_left(self):
        """Return how many places are still open."""
        return self.capacity - len(self._enrolled)

    def enrol(self, student):
        """
        Enrol a student on the course.
        Refuses (raises EnrollmentError) if the student is already
        enrolled, or if the course is already full.
        """
        if self.is_enrolled(student):
            raise EnrollmentError(
                f"Cannot enrol {student}: already enrolled on {self.code}."
            )
        if self.is_full():
            raise EnrollmentError(
                f"Cannot enrol {student}: {self.code} is full "
                f"({self.capacity}/{self.capacity} places taken)."
            )
        self._enrolled.append(student)
        print(f"Enrolled {student} on {self.code}.")

    def drop(self, student):
        """
        Remove a student from the course.
        Refuses (raises EnrollmentError) if the student is not enrolled.
        """
        if not self.is_enrolled(student):
            raise EnrollmentError(
                f"Cannot drop {student}: not enrolled on {self.code}."
            )
        self._enrolled.remove(student)
        print(f"Dropped {student} from {self.code}.")

    def display(self):
        """Print a clear summary of the course for staff to view."""
        print(f"\nCourse: {self.code} - {self.title}")
        print(f"Places: {len(self._enrolled)}/{self.capacity} filled "
              f"({self.places_left()} open)")
        if self._enrolled:
            print("Enrolled students:")
            for student in self._enrolled:
                print(f"  - {student}")
        else:
            print("Enrolled students: (none yet)")

    def __str__(self):
        return f"{self.code}: {self.title} ({len(self._enrolled)}/{self.capacity})"


def demo():
    """Demonstrates normal use and invalid actions being refused."""

    print("=== Creating a course with a small capacity ===")
    course = Course("CSC2105", "Object-Oriented Programming Using Python", capacity=3)
    course.display()

    print("\n=== Enrolling several students (normal use) ===")
    alice = Student("Alice")
    bob = Student("Bob")
    carol = Student("Carol")

    course.enrol(alice)
    course.enrol(bob)
    course.display()

    print("\n=== Attempting a duplicate enrolment (should be refused) ===")
    try:
        course.enrol(alice)
    except EnrollmentError as e:
        print(f"Refused: {e}")

    print("\n=== Filling the course, then trying to enrol past capacity ===")
    course.enrol(carol)  # fills the course (3/3)
    course.display()

    dave = Student("Dave")
    try:
        course.enrol(dave)
    except EnrollmentError as e:
        print(f"Refused: {e}")

    print("\n=== Dropping a student ===")
    course.drop(bob)
    course.display()

    print("\n=== Now there is a place again, so Dave can enrol ===")
    course.enrol(dave)
    course.display()


if __name__ == "__main__":
    demo()
