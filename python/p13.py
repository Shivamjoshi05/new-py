tea_verities = ["black","green","oolong","white"]
print(tea_verities[2])
print(tea_verities[0])

print(tea_verities[-3])

tea_verities[3]="herbal"

print(tea_verities)

print(tea_verities[1:2])
# tea_verities[1:2] = "lemon"
print(tea_verities)
# ['black', 'l', 'e', 'm', 'o', 'n', 'oolong', 'herbal']

tea_verities[1:2] = ["lemon"]
print(tea_verities)

for i in tea_verities:
    print(i,end="-")

tea_verities_copy = tea_verities.copy()
tea_verities_copy.append("Masala")
print(tea_verities_copy)

square = [x**2 for x in range(11)]
print(square)