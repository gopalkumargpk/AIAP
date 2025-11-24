# TASK 3 - COMPLETE REFACTORING (Class Improvement)
# LEGACY CODE
class Student:
    def __init__(self, n, a, m1, m2, m3):
        self.n = n
        self.a = a
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    def details(self):
        print("Name:", self.n, "Age:", self.a)

    def total(self):
        return self.m1 + self.m2 + self.m3


# REFACTORED CODE
class Student:
    """Represents a student and their academic details."""

    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks   # list of marks

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

    def total_marks(self):
        return sum(self.marks)


# Creating a student object
student1 = Student("HARSH", 21, [85, 90, 88])

# Printing student details
student1.show_details()

# Printing total marks
print("Total Marks:", student1.total_marks())
