def add_greeting(cls):
    cls.greet = lambda self: "Hello from Decorator!"
    return cls 

@add_greeting 
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Hamza", 19)
print(p.greet())