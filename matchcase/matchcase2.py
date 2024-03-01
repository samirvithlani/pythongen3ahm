day = input("select day")

match day:
    case "monday" | "MONDAY":
        print("you have selected monday")
    case "tuesday":
        print("you have selected tuesday")
    case _:
        print("invalid choice")        