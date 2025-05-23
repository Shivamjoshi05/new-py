class Employee:
    company ="HP"
    def get_salary(self): # Self is important here because self is a way to reference the obj of the class which is being created 
        print(self)
        return 34000

e1=Employee()
print(e1.get_salary())

e2=Employee()
print(e2.get_salary())

print(e2.company)