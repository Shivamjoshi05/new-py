d = str(input("Enter day: "))

match d:
    case "monday":
        print("start of week")
    case "tuesday":
        print("normal day")
    case "wednesday":
        print("midweek")
    case "thursday":
        print("normal day")
    case "friday":
        print("normal day")
    case "saturday":
        print("weekend")
    case "sunday":
        print("weekend")
    case _:
        print("invalid input")