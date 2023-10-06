#0 , 1 1 2 3 5 8 13 21 34 55 89 144
a = 0
b = 1
sum =0
print(a,b,end= " ")
#
for i in range(1,10):
    #0 = 0 + 1 sum =1
    # = 1 + 1 sum =2
    # = 1 + 2 sum =3
    # = 2 + 3 sum =5
    sum = a + b
    print(sum,end= " ")
    #a =1
    #a = 1
    #a = 2
    a = b
    #b = 1
    #b = 2
    #b = 3
    b = sum
