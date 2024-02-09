def test():
    print("This is a test function")
    print("without return type without args")


test()    

def add(a,b):
    #c = a+b
    return a+b
    #return c


ans = add(100,20)    
print("Addition is:",ans)



def getUserData():
    name = input("Enter your name:")
    print("Name is:",name)
    age = int(input("Enter your age:"))
    print("Age is:",age)
    


getUserData()    
    
    
    