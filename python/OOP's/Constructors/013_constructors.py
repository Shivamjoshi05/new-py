class student:
    def __init__(self,math,cs,bio):
        self.math=math
        self.cs=cs
        self.bio=bio
    def average(self):
        return (self.math+self.cs+self.bio)/3
    def get_info(self):
        print(f"Marks of math is {self.math}")
        print(f"Marks of Computer Science is {self.cs}")
        print(f"Marks of Biology is {self.bio}")
        print(f"the Average is {self.average()}")
    
S = student(89,90,79)
S.get_info()