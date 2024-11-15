# Write a program to define a class Student with attributes like name and age, and create objects to represent different students.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 19)
student1.display_info()
student2.display_info()
student3.display_info()
