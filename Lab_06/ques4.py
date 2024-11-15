# Create a class named 'Student' with String variable 'name' and integer variable 'roll_no'. Assign the value of roll no as '2' and that of name as "John" by creating an object of the class Student. in python

class Student:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no

student1 = Student("John", 2)
print(f"Name: {student1.name}, Roll No: {student1.roll_no}")
