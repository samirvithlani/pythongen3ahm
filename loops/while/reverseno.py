no = int(input("Enter a number: "))
temp= no
# 123
# #123 % 10 =3
# 12 % 10 = 2
# 1 % 10 = 1

#123//10 = 12
#12//10 = 1
rem = 0
sum =0
#123 > 0 TRUE
#12 > 0 TRUE
#1 > 0 TRUE
while no>0:
    # 123 % 10 = 3
    # 12 % 10 = 2
    # 1 % 10 = 1
    rem = no % 10
    # 0 * 10 + 3 = 3
    # 3 * 10 + 2 = 32
    # 32 * 10 +1 = 321  
    sum = sum* 10 + rem
    # 123 // 10 = 12
    # 12 // 10 = 1
    # 1 // 10 = 0
    no = no // 10
    

print("Reverse number is: ",sum)    
    

if temp == sum:
    print("Palindrome")
else:
    print("Not Palindrome")        
    