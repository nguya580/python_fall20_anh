# %% declare class Student

class Student:
    def __init__(self, school, first, last):
        self.school = school
        self.first = first
        self.last = last

    def updated_school(self, updated_school):
        self.school = updated_school

    def updated_first(self, updated_first):
        self.first = updated_first

    def update_last(self, update_last):
        self.last = update_last

    # __str__ is used for creating output for end user
    # __str__ will return a human readable string.
    def __str__(self):
        return f"{self.first} {self.last} is a student of {self.school}."

student1 = Student("Newbury College", "Anh", "Nguyen") # (self, school, first, last)

print(student1)

student1.updated_school("Suffolk University")

print(student1)

# %%
# Challenge #1 add an class wide attribute student count and give every student an ID
# Challenge #2 add a behavioral method to the stud

import random

class Student:

    count = 0

    def __init__(self, school, first, last):
        self.school = school
        self.first = first
        self.last = last

        Student.count += 1

    def updated_school(self, updated_school):
        self.school = updated_school

    def updated_first(self, updated_first):
        self.first = updated_first

    def update_last(self, update_last):
        self.last = update_last

    def print_id(self):
        self.id = f"{self.first[0:3].lower()}{self.last[0:3].lower()}{random.randint(100,999)}"
        return self.id

    def statement(self, statement):
        self.statement = statement
        return f"{self.first} {self.last} wants to say that '{self.statement}'"

    # __str__ is used for creating output for end user
    # __str__ will return a human readable string.
    def __str__(self):
        return f"{self.first} {self.last} is a student of {self.school}."

student1 = Student("Suffolk University", "Anh", "Nguyen")
student2 = Student("NESAD", "Linh", "Le")
student3 = Student("NESAD", "Phuong", "Nguyen")

print(student1.print_id(), student2.print_id(), student3.print_id())

print(student3.statement("I like my classmates."))

# %% Sub-class

class GradStudent(Student):

    count = 0

    def __init__(self, school, degree, first, last):
        super().__init__(school, first, last)
        self.degree = degree
        GradStudent.count += 1

    def show_degree(self):
        return f"{self.first} {self.last} is a student in the {self.degree} program at {self.school}."

    def print_id(self):
        self.id = f"{self.first[0:3].lower()}{self.last[0:3].lower()}{random.randint(100,999)}"
        return self.id

    # __str__ is used for creating output for end user
    # __str__ will return a human readable string.
    def __str__(self):
        return f"{self.first} {self.last} is a graduate student of {self.school}."

grad_student1 = GradStudent('Parsons', 'MFA', 'Teddy', 'Nguyen')
grad_student1.show_degree()
grad_student1.print_id()

# %% Challenge #4 Create a School Class that has Students as attributes

class School:

    def __init__(self, name):
        self.name = name
        self.students = []

    def enroll_student(self, student):
        self.students.append(student)

    def print_student(self):
        print(f"Here is a list of students in {self.name}:\n")
        for student in self.students:
            print(student)

schoolOfThoughts = School("School of Thoughts")

schoolOfThoughts.enroll_student(student1)
schoolOfThoughts.enroll_student(student2)
schoolOfThoughts.enroll_student(student3)
schoolOfThoughts.enroll_student(grad_student1)

schoolOfThoughts.print_student()
