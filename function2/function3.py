def isAvailable(users,name):
    flag = False
    for i in users:
        if i == name:
            flag = True
            break
    
    return flag    


x = isAvailable(["ram","lakshman","sita","amit"],"rama")
print("isAvailable:",x)