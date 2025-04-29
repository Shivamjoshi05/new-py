a = int(input("Enter 1st side of triangle"))
b = int(input("Enter 2nd side of triangle"))
c = int(input("Enter 3rd side of triangle"))

if(a==b and a==c and c==b):
    print("the triangle is Equilateral")
elif((a==b and a!=c) or (b==c and b!=a)or(a==c and a!=b)):
    print("the triangle is isoscelus")
else:
    print("the triangle is scalanes")