#match case

print("enter your choice")
print("1 for goa \n 2 for delhi \n 3 for mumbai \n 4 for kolkata")
choice = int(input())

match choice:
    case 1:
        print("you have selected goa")
    case 2:
        print("you have selected delhi")
    case 3:
        print("you have selected mumbai")
    case 4:
        print("you have selected kolkata")
    
    case _:
        print("invalid choice")                
