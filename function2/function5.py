def matchList(list1,list2):
    flag = True
    if len(list1) != len(list2):
        flag = False
    else:
        for i in range(len(list1)):
            if list1[i]!=list2[i]:
                flag = False
                break    
    
    return flag        
    


x = matchList([1,2,3],[1,20,3])
print("matchList:",x)