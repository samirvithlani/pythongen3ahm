#if with lambda

# def findmax(a,b):
#     if a>b:
#         return a
#     else:
#         return b


findMax = lambda a,b :a if a >b else b
print(findMax(10,20))


findmax1 = lambda a,b, c : a if a>b and a >c else b if b > c else c
print(findmax1(10,20,30))


