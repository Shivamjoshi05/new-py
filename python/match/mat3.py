cat = str(input("Enter your catagory(Electronics/clothing/grocery): "))

match cat:
    case "electronics":
        a = str(input("What do you want(phone/laptop)"))
        match a:
            case "phone":
                ph = str(input("Which Phone?\n"))
                print(ph," Phone is avalable at the store")
            case "laptop":
                la = str(input("Which Laptop"))
                print(la," Laptop is avalable at the store")
            case _:
                print(a,"oops!!  currently out of stock")
    case "clothing":
        b = str(input("Please select your section(male/female/kids): "))
        match b:
            case "male":
                print("male section is on 1st floor")
            case "female":
                print("Female section is on 2nd floor")
            case "kids":
                print("Kids section is on 3rd floor")
            case _:
                print("Please enter valid section")
    case "grocery":
        c = str(input("What do you want (vegitables/fruits): "))
        match c:
            case "vegitables":
                veg = str(input("Which vegitable do you want: "))
                print(veg,"is avaiblable in fresh condition")
            case "fruits":
                fruit = str(input("which fruit do you want: "))
                print(fruit,"is available in fresh condition")
            case _:
                print("Please enter valid choice")
    case _:
        print("please enter valid choice")
        