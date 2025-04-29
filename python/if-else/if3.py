a = int(input("Enter age: "))

if(0<=a<=12):
    print("the victim is child")
elif(13<=a<=19):
    print("the victim is Teenager")
elif(20<=a<=64):
    print("the victim is adult")
else:
    print("the victim is senior")