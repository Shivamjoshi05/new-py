a = ["apple","banana","orange","apple","mango"]

unique_item = set()

for item in a:
    if item in unique_item:
        print("Duplicate: ",item)
        break
    unique_item.add(item)
