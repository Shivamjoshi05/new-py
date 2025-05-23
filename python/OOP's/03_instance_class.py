class Employee:
    company = "Asus"
    def __init__(self,salary,name,bond,company):
        self.salary=salary
        self.name=name
        self.bond=bond
        self.company=company
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of Employee is {self.name},salary is {self.salary} for {self.bond} years in {self.company}")
    
e1=Employee(34000,"Jhon Doe",3,"tesla")
e1.get_info()
print(e1.company)#it will print instance attribute i.e tesla
print(Employee.company)#this will print Class attribute i.e Asus
print(dir(e1))