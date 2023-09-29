age =int(input("Enter your age: "))

if age>=18:
    print("You are eligible to vote")
    
    if age>=21:
        print("You are eligible to marry")
    else:
        print("You are not eligible to marry")

else:
    print("You are not eligible to vote")  
    
    if age>=16:
        print("You are eligible to drive")    
    else:
        print("You are not eligible to drive")          