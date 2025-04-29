country = str(input("Enter Country: "))
match country:
    case "USA":
        state = str(input("Enter state: "))
        match state:
            case "California":
                print("West Coast")
            case "New york":
                print("East Coast")
            case _:
                print("Other state in USA")
    case "India":
        s = str(input("Enter state: "))
        match s:
            case "Maharashtra":
                print("Western India")
            case "Assam":
                print("Northeast india")
            case _:
                print("Other state in India")
    case _:
        print("Country Not Found!!")