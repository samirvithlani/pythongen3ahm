no1 = int(input("Enter the first number: "))
no2 = int(input("Enter the second number: "))

def smartDiv(func): #func = div
    
    def inner():
        if no2 == 0:
            print("Cannot divide by zero")
        else:
            func()
    return inner

@smartDiv
def div():
    print("div...",no1//no2)                
    
    

div()    