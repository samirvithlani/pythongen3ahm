def checkName(name):
    flag  = True
    for i in name:
        if not (ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122 or ord(i)==32):
            flag = False
    
    return flag    
            

x = checkName("richa")        
print(x)
    
    