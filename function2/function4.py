def isAvailable(users,name):
    cnt = users.count(name)
    return cnt


x = isAvailable(["ram","lakshman","sita","amit"],"rama")
if x>0:
    print("Available")
else:
    print("Not available")    
    