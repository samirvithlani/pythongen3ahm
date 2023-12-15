def convertList(tup):
    
    return list(tup)

x = convertList((1,2,3,4,5,6,7,8,9,10))
print(x)



def sumoflist(num):
    #check data type...
    sum = 0
    for i in num:
        #check datatupe of i
        sum = sum + i
    
    return sum


def sumpfList2(num):
    return sum(num)


ans = sumoflist([1,2,3,4,5,6,7,8,9,10])
print(ans)
    
    
ans1 = sumpfList2([1,2,3,4,5,6,7,8,9,10])
print(ans1)    