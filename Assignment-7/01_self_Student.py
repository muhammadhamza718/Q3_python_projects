class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name} Age: {self.age}")

s1 = Student("Hamza", 20)
s1.display()