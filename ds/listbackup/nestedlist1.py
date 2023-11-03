data = [[10,20,30],[40,50,60],[70,80,90]]

# print(data[0])
# print(data[0][0])
# print(data[2][1])


sum =0
for i in range(0,len(data)):
    sum =0
    for j in range(0,len(data[i])):
        print(data[i][j],end=" ")
        sum = sum + data[i][j]
    
    print("sum = ",sum,end=" ")    
    
    print()    


# for i in data:
#     for j in i:
#         print(j,end=" ")
    
#     print()    

# x = [10,20,40]

# m = max(x)
# print(m)


# a shopkeep has 7 days record of sales it contains morning sales and evening sales ,
# we need to find total weekly sales and average sales of morning and evening
#and  max sales unit from week

# 10, 230, 70, 80, 90, 100, 110