# def outer():
#     print("Outer function 1")
#     def inner():
#         print("Inner function")
    
#     print("Outer function 2")
#     inner()


# outer()



# def outer():
#     print("Outer function 1")
#     def inner(no1,no2):
#         print("Inner function")
#         print("no1 = ",no1)
#         print("no2 = ",no2)
    
#     print("Outer function 2")
#     inner(100,20)


# outer()

# def outer(a,b,c):
#     print("Outer function 1")
#     print("a = ",a)
#     print("b = ",b)
#     print("c = ",c)
    
    
#     def inner(no1,no2):
#         print("Inner function")
#         print("no1 = ",no1)
#         print("no2 = ",no2)
#         print("a = inner",a)
#         print("b = inner",b)
#         print("c = inner",c)
    
#     print("Outer function 2")
#     inner(100,20)

# outer(10,20,30)


def outer(a,b,c):
    print("Outer function 1")
    print("a = ",a)
    print("b = ",b)
    print("c = ",c)
    
    
    def inner(no1,no2):
        print("Inner function")
        print("no1 = ",no1)
        print("no2 = ",no2)
       
        return no1+no2
       
    print("Outer function 2")
    sum = inner(100,20)
    print("Sum = ",sum)
    return sum + a + b + c

x = outer(10,20,30)
print("x = ",x)