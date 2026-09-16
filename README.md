# Question-8
OOP  course enrollment system 
A department runs courses that only have a limited number of places.
Each course has a course code, a title, a maximum capacity, and a list of students who are currently enrolled. For this stage you may record students by name; richer student records can come later.
A student may enrol on a course or leave it. Enrolment must be refused if the course is already full, or if that student is already on the list. In both cases the system should make the reason clear.
Staff need to know how many places are still open and to see a clear display of the course: code, title, how full it is, and who is enrolled.which will make it easier for the user to use.
A demonstration should create a course with a small capacity, enrol several students, attempt a duplicate enrolment and an enrolment after the course is full, drop a student, and print the course

## Enrollment System Implementation

This project is a small object-oriented course enrollment system written in Python. The implementation is in [Enrollment.py](Enrollment.py) and models students and courses as separate objects.

### Features

- Stores a student's registration number, name, and current courses.
- Stores a course code, title, maximum capacity, and enrolled students.
- Enrolls students only when they are not already enrolled and a place is available.
- Drops enrolled students and updates the student's course list at the same time.
- Calculates the number of places still available.
- Prints readable student and course summaries.
- Gives a clear message when an enrollment or drop operation cannot be completed.

### Main Classes

#### `Student`

Create a student with a registration number and name:

```python
student = Student("S001", "Wilson")
```

The `courses` list contains the `Course` objects in which the student is currently enrolled. The `enrolled_courses()` method prints each course code and title.

#### `Course`

Create a course with its code, title, and maximum capacity:

```python
course = Course("CSE101", "Introduction to Computer Science", 2)
```

The course provides these operations:

| Method | Purpose |
| --- | --- |
| `enroll_student(student)` | Adds a student if they are not already enrolled and the course is not full. Returns `True` on success and `False` on failure. |
| `drop_student(student)` | Removes an enrolled student. Returns `True` on success and `False` if the student is not enrolled. |
| `available_places()` | Returns the number of unfilled places. |
| `str(course)` | Produces a summary containing the course code, title, capacity, and enrolled student names. |

Enrollment is recorded in both directions: the student is added to `course.enrolled_students`, and the course is added to `student.courses`. Dropping a student removes both links.

### Validation Rules

1. A duplicate enrollment is refused with an explanation.
2. Enrollment is refused when `available_places()` is zero.
3. A student can only be dropped if they are currently enrolled.
4. A successful drop creates a place that another student can use.

### Run the Demonstration

From the project directory, run:

```bash
python Enrollment.py
```

The demonstration creates a course with a capacity of two, enrolls two students, attempts to enroll a third student after the course is full, prints the course, drops one student, enrolls the third student, and prints the updated course.

### Example Output

```text
Student wilson enrolled in CSE101.
Student baker enrolled in CSE101.
Enrollment failed: Course CSE101 is full.
Course Code: CSE101
Title: Introduction to Computer Science
Capacity: 2/2
Enrolled Students: wilson, baker
Student wilson dropped from CSE101.
Student john enrolled in CSE101.
```

### Project Files

- [Enrollment.py](Enrollment.py): Student and Course classes, plus the runnable demonstration.

- [README.md](README.md): Assignment question and project documentation.
