class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self.salary = salary
        self.ssn = ssn

emp = Employee("Hamza", 70000, "123-45-6789")
print(emp.name)
print(emp.salary)
print(emp.ssn)