no = int(input("Enter a number: "))
rem =0
sum=0
mul=1
while no>0:
    rem = no % 10
    sum = sum + rem
    mul = mul * rem
    no = no // 10
    

print("Sum of digits is: ",sum)
print("Product of digits is: ",mul)    