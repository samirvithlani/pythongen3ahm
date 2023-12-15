def printList(users):
    if type(users) == type([]):
        for i in users:
            print(i)
    else:
        print("Invalid argument")        


#printList(["ram","shyam","hari"])        
printList(("ram","shyam","hari"))
#printList("ram")        
#printList(100)