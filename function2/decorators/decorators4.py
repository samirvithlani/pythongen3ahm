def smartdiv(func):
    
    def inner(no1,no2):
        print("no1 is",no1)
        print("no2 is",no2)
        if no2 ==0:
            print("Can't divide by zero")
        else:
            func()
    
    return inner


@smartdiv
def div():
    print(10/2)            
    

div(100,10)    