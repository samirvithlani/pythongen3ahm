def getMaxWordFromString(data):
    word = data.split()
    return max(word,key=len)



x = getMaxWordFromString("i love my country and my country is india")
print(x)
    