def getEventList(*args):
    return [i**2 for i in args]


x = getEventList(1,2,3,4,5)
print(x)