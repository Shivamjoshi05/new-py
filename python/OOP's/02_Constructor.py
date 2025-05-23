class Employee:
   
    def __init__(self,salary,name,bond):
        self.salary=salary
        self.name=name
        self.bond=bond
    def get_salary(self):
        return self.salary
    def get_info(self):
        print(f"The name of Employee is {self.name},salary is {self.salary} for {self.bond} years")
    
e1=Employee(34000,"Jhon Doe",3)
e1.get_info()
e1.get_salary()