class Employee:
    company = "HP"
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def print_info(self):
        info=(f"the name is {self.name} and the salary is {self.salary}")
        print(info)
    @staticmethod
    def sum(a,b):
        return a+b
    @classmethod
    def print_company(cls):
        print(cls.company)
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company

e1=Employee("Jack",3455)
e2 = Employee("jill",3455)
print(Employee.company)
print(Employee.name)
e1.print_info()
e2.print_info()
print(e1.sum(5,8))
e1.print_company()
e1.change_company("Acer")
e1.print_company()