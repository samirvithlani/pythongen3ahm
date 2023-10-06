#153 --> 1 + 5 + 3 = 1 + 125 + 27 = 153
#1634 --> 1 + 256 + 81 + 1296 = 1634
no = int(input("Enter a number: "))
temp = no
digitcount =0
while temp>0:
    temp = temp // 10
    digitcount = digitcount + 1
    

rem= 0
sum = 0
while no>0:
    rem = no % 10
    sum = sum + rem ** digitcount
    no = no // 10


print("Sum of cube of digits is: ",sum)    
    