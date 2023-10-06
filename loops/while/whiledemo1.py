#123 --> 3 # 1445 #4
#123 // 10 =12
#12 // 10 = 1
#1 // 10 = 0

#4578
#4578 // 10 = 457
#457 // 10 = 45E
#45 // 10 = 4
#4 // 10 = 0

no = int(input("Enter a number: "))
# i =1
# while(i<=10):
#     print(i)
#     i+=1

count =0
while(no>0):
    no = no // 10
    count+=1


print("Total digits are: ",count)    