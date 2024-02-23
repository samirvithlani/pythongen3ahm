def smartdiv(func):
    
    def inner(no1,no2):
        print("no1 is",no1)
        print("no2 is",no2)
        if no2 ==0:
            print("Can't divide by zero")
        else:
            func(no1,no2) #div
    
    return inner


@smartdiv
def div(x,y):
    print("x is",x)
    print("y is",y)
    print(x/y)            
    

div(100,10)    