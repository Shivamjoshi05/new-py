a = int(input("Enter marks: "))
match a:
    case _ if(90<=a<=100):
        print("Outstanding")
    case _ if(75<=a<=89):
        print("Very Good")
    case _  if(50<=a<=74):
        print("Good")
    case _ if(0<=a<=49):
        print("fail")
    case _ :
        print("Invalid Input")