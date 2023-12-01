#[],(),{}

# data = {} # empty dictionary
# print(type(data))
# print(data)

data = {"MON":100,"TUE":200,"WED":300,"THU":400,"FRI":500,"SAT":600,"SUN":700}
print(data)

k = data.keys()
print(k)
v = data.values()
print(v)

kv = data.items()
print(kv)

for i in data.items():
    for j in i:
        print(j)
    print("-----")