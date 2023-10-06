#5 3 4 2 1
no = int(input("Enter a number: "))
mul =1
# 1,2,3
for i in range(1,no+1):
    #1 = 1 * 1 = 1
    #1 = 1 * 2 = 2
    #2 = 2 * 3 = 6
    #6 = 6 * 4 = 24
    #24 = 24 * 5 = 120
    mul = mul * i

print("Multiplication of first ",no," numbers is ",mul)    

    
    