def isValid(name):#ram
    flag = True
    for i in range(0,len(name)):
        
        # if name[i] == " ":
        if " " in name[i]:
            flag = False
            break
        else:
            flag = True
        

    return flag        
            


x = isValid("ra m")        
print(x)