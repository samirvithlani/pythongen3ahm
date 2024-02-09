def checkPalindrome(*args):
    flag =True
    for i in args:
        if i != i[::-1]:
            flag = False
            break

    return flag        

        
        


x = checkPalindrome("madam","naman","racecar","madam")
print("checkPalindrome:",x)

