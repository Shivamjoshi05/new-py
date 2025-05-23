class point():
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def sum(self,p):
        return point((self.x + p.x),(self.y+p.y))
    def print_point(self):
        print(f"X is {self.x} and Y is {self.y}")
    def __add__(self,p):
        return point((self.x +p.x),(self.y+p.y))

p1 = point(2,4)
p2 = point(4,6)


p = p1.sum(p2)
p.print_point()


