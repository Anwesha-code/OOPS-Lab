# Create two classes Teacher and Author, each with their own description() method to describe the profession. Then, create a subclass TutorAuthor that inherits from both Teacher and Author. Use this subclass to call the description() method from each parent class. Use the super() function to resolve any conflicts if necessary.

class Teacher:
    def description(self):
        print("I am a teacher and I educate students.")

class Author:
    def description(self):
        print("I am an author and I write books.")

class TutorAuthor(Teacher, Author):
    def description(self):
        super().description()  
        Author.description(self)  

tutor_author = TutorAuthor()
tutor_author.description()
