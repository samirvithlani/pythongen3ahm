sal = 12000

if sal>=100000:
    print("You are eligible for 2 wheeler loan")
    
    if(sal>=200000):
        print("You are eligible for 4 wheeler loan")
        
        if(sal>=500000):
            print("You are eligible for home loan")    
        else:
            print("You are not eligible for home loan")    
    else:
        print("You are not eligible for 4 wheeler loan")
else:
    print("please do work hard and increase your salary")
print("Thank you for banking with us")                