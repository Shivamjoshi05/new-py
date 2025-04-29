n = int(input("Enter Number: "))
is_prime = True
print("the number is prime")
if n > 1:
    for i in range(2,n):
        if (n % i)==0:
            is_prime = False
            break
print("number is not prime number")
