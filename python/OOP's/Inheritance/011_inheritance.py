class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_per(self):
        print(f"name: {self.name}")
        print(f"age: {self.age}")
class Student(Person):
    def __init__(self,name,age,roll):
        super().__init__(name,age)
        self.roll = roll
    def get_info(self):
        self.get_per()
        print(f"Roll no: {self.roll}")

S = Student("raj",19,34)
S.get_info()
