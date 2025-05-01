def fact(num):
    facts = 1
    while num>0:
        facts = facts * num
        num -= 1
    return facts

factorial = fact(5)
print(factorial)
    
