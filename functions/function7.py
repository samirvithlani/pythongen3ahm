def mergeDict(dict1, dict2):
    dict1.update(dict2)
    #return dict1
    return dict1 | dict2


x = mergeDict({1:"a",2:"b"},{3:"c",4:"d"})
print(x)
    

def findMax(users):
    return max(users)

x = findMax([1,2,3,4,5,6,7,8,9,10])    
print(x)


def isPalindrome(name):
    return name == name[::-1]

print(isPalindrome("madam"))
    
    