def getEvenList(*args):
    x =[]
    for i in args:
        if i % 2 == 0:
            x.append(i)
    
    return x


ans = getEvenList(10,1,34,5)
print(ans)        
            