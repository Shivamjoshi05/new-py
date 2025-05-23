class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
      
    def get_info(self):

        print(f"the area of with length {self.length} and width {self.width} is {self.area()} ")

R = Rectangle(5,6)
R.get_info()