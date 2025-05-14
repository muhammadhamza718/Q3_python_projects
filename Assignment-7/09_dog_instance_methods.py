class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        print(f"{self.name} says Woof!")

d = Dog("Rex", 5 , "German Shepherd")
d.bark()