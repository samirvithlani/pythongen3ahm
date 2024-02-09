def checkDuplicate(*args):
    flag = False
    #0
    for i in range(len(args)):
        #j =1,2,3
        for j in range(i+1,len(args)):
            #10 ==20
            #10 ==30
            #10 ==40
            #10 ==10
            if args[i] == args[j]:
                flag = True
                break
        if flag:
            break
    return flag    
                



x = checkDuplicate(10,20,30,40,10,20,30,40)
print("checkDuplicate:",x)
