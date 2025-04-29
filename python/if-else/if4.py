import cmath

a = int(input("Enter 1st no. : "))
b = int(input("Enter 2nd no. : "))
c = int(input("Enter 3rd n0. : "))

if (a>b and a>c):
    print("the number ",a,"is greater than ",b,"and",c)
elif(b>a and b>c):
    print("the number ",b,"is greater than ",a,"and",c)
else:
    print("the number ",c,"is greater than ",a,"and",b)

print(max(a,b,c))