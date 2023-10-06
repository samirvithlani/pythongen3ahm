base = int(input("Enter a base: "))
power = int(input("Enter a power: "))
m =1
#2 ,3
for i in range(1,power+1):
    #1 = 1 * 2 = 2
    #2 = 2 * 2 = 4
    #4 = 4 * 2 = 8
    m = m * base

print("Power of ",base,"^",power," is ",m)    