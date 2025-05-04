#F-string

letter = "hey my name is {} and i am from {}"

name = "Shivam"
country = "India"

print(letter.format(name,country))

print(f"hey my name is {name} and i am from {country}")

price = 49.099
txt = f"for only{price:.2f} Dollors"
print(txt)