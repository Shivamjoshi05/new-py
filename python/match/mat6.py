file = str(input("Enter file type: "))
ext= str(input("enter file extention"))
match file:
    case "image":
        match ext:
            case "png"|"jpg"|"jpeg":
                print("valiid image format")
            case _:
                print("Invalid format")
    case "document":
        match ext:
            case "pdf"|"docx":
                print("valid extention")
            case _:
                print("invalid input")
    case "audio":
        match ext:
            case "mp3"|"wav":
                print("Valid input")
            case _:
                print("invalid input")
    case _:
        print("Invalid input")