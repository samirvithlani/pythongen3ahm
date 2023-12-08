data1 = {"jay","bhavya","parth","amit"}
data2 = {"jay","priya"}



x = data1.union(data2)
print(x)

#data1 - data2
x = data1.difference(data2)
print("x---",x)

x = data1.intersection(data2)
print(x)   


x = data1.symmetric_difference(data2)
print(x)

