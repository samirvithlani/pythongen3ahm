
#func -->is current function object
def order(func): #3 func = throw_party
    print(func)
    
    def inner(): #5
        print("Ordering a pizza")#6
        func() #calling the function #7 throw_party()
    
    return inner  #4  


@order #2
def throw_party():#8
    print("Throwing a party")#9


throw_party() #1