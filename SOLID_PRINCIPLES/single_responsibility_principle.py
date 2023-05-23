class Employee:
    def __init__(self, name, age, salary) -> None:
        self.name = name
        self.salary= salary
        self.age = age
    
    def __str__(self) -> str:
        return ",".join([self.name, self.age, self.salary])

'''
This class violates the single responsibility principle 
as this class is being used for multiple purpuses
1. saving employees
2. loading employees
3. add emplyoess
3. printing employees
'''

class Employees:

    def __init__(self):
        self.employees = []
        
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def save_employees(self, filePath):
        with open(filePath) as f:
            f.writelines(self.employees)

    def load_employees(self, filepath):
        with open(filepath, "r") as f:
            for line in f.readlines():
                name, age, salary = line.split(",")
                self.employees.append(Employee(name, age, salary))

    def print_employee(self):
        for e in self.employees:
            print(e)