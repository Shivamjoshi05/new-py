def large(a,b,c):
    if(a>b and a>c):
        print(a,"is greater")
    elif(b>a and b>c):
        print(b,"is greater")
    else:
        print(c,"is greater")

result = large(3,4,1)
print(result)