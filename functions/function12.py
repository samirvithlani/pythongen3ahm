def getSum(*args):
    
    sum = 0
    for i in args:
        sum = sum + i
    
    return sum    
    

x = getSum(10,20,30,40,50)
print(x)
