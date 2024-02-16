#map -->will return all data...

data = ["ram","shyam","sharma"]

# x = [i.upper() for i in data]
# print(x)

upperData = list(map(lambda x:x.upper(),data))
print(upperData)

marks = [10,20,30,45,32]
newmark = list(map(lambda x:x+5,marks))
print(newmark)

sales = [[10,20],[20,30],[15,25]]

sales1 = list(map(lambda x:list(map(lambda y:y+10,x)),sales))
print(sales1)
