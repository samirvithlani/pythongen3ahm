#1,2,3
for i in range(1,6):
    for j in range(1,i+1):
        print((j-1)%2,end=",")
    
    print()            



# for i in range(1,6):
#     for j in range(5,i-1,-1):
#         print("*",end=" ")
    
#     print()    
    
    

for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
    

k=0
for i in range(1,6):
    for i in range(1,i+1):
        k+=1
        #1
        #2 3
        print(k ,end=" ")
    
    print()    
            