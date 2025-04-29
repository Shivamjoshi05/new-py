w = str(input("Enter Word: "))
vol = "aeiou"
vol_count = 0

for char in w:
    if char in vol:
        vol_count += 1
print(vol_count)