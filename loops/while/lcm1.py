x =int(input("Enter first number: "))
y= int(input("Enter second number: "))
greater =0

#6, 4

if x>y:
    greater = x
else:
    greater = y    

lcm =0    

#6
while True:    
    #  6 % 6 ==0 and 6 % 4 ==0      
    #  7 % 6 ==1 and 7 % 4 ==3
    #  8 % 6 ==2 and 8 % 4 ==0
    #  9 % 6 ==3 and 9 % 4 ==1
    # 10 % 6 ==4 and 10 % 4 ==2
    # 11 % 6 ==5 and 11 % 4 ==3
    # 12 % 6 ==0 and 12 % 4 ==0
    if greater %x ==0 and greater %y ==0:
        #4
        lcm = greater
        break
    greater = greater + 1
    #7

print("LCM of ",x," and ",y," is: ",lcm)    