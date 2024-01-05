def checkString(name):
    name = name.strip()
    flag =False
    for i in name:
        if " "in i:
            flag = True
            break
    
    return flag    
        


x = checkString(" sachin-tendulkar ")        
if x == True:
    print("String contains space")

else:
    print("String does not contains space")    