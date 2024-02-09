def isValid(name):
    flag = True
    for i in name:
        if i == " ":
            flag = False
            break
    
    return flag

x = isValid("ram chandra")    
print("isValid:",x)