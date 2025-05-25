class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def __str__(self):
        return f"the name is {self.name} and salary is {self.salary}"
    def __repr__(self):
        return f"name: {self.name}\nsalary: {self.salary}"
    def __len__(self):
        return len(self.name)
e1 = Employee("Jhon",40000)
print(e1.name,e1.salary)
print(str(e1))
print(repr(e1))
print(len(e1))