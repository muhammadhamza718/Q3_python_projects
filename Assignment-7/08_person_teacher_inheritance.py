class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)
        self.subject = subject

t = Teacher("Hamza", 19, "Biology")
print(t.name)
print(t.age)
print(t.subject)