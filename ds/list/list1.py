#data =[] #empty list
data = ["java","python","c","c++","ruby","perl","php","javascript"]

print(data[0])
data[0] = "java8"
print(data)

x = len(data)
print(x)

data.append("scala")

data.extend(["go","swift","kotlin"])
#data.extend("kotlin")

data.insert(2,"basic")

print(data)
# for i in data:
#     print(i)

# for i in range(0,x):
#     print(data[i])

# print(type(data))