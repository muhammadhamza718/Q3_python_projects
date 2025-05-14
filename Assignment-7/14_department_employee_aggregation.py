class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Department:
    def __init__(self, employee):
        self.employee = employee

emp = Employee("Hamza", 70000)
dep = Department(emp)
print(dep.employee.name)
print(dep.employee.salary)