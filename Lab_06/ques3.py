# Write a program to create a class called "Person" with a name and age attribute. Create two instances of the "Person" class, set their attributes using the constructor, and print their name and age. in python

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person1.display_info()
person2.display_info()
