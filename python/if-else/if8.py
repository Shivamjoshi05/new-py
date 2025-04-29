g = "gold"
s = "silver"
n = "none"
metal = str(input("Enter your choice(Gold/Silver/none) : "))
rate = float(input("Enter your budget: "))
if(metal == g):
    if(rate==1000):
        discount= rate *(20/100)
        price = rate - discount
        print("You will get 20 percent off on 1000 Gold price \n the price will become: ",price)
    elif(rate<=1000):
        discount = rate * (15/100)
        price = rate - discount
        print("You will get 15 percent off on below 1000 Gold price \n the price will become: ",price)
elif(metal == s):
    if(rate == 1000):
          discount= rate *(10/100)
          price = rate - discount
          print("You will get 10 percent off on 1000 Silver price \n the price will become: ",price)
    elif(rate <= 1000):
          discount = rate * (5/100)
          price = rate - discount
          print("You will get 5 percent off on below 1000 Silver price \n the price will become: ",price)
elif(metal == n):
     print("\nThank You!!!")