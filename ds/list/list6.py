x = ["amit","raj","mohan","sohan","ram","shyam"]
fillist =[]

for i in x:
    #print(i)
    if len(i)>3:
        fillist.append(i.upper())

print(fillist)       


fillist2 =[]

for i in x:
    fillist2.append(i.upper())

print(fillist2)    


data = ["mark1","rober#","tom3","amit-thakkar","jay","raj"]
fildata =[]

for i in data:
    if i.isalpha():
        fildata.append(i)

print(fildata)        

data1 =  ["AmiT","Neha","ram","sita","Shyam"]
fildata1 =[]

for i in data1:
    if i.islower():
        fildata1.append(i)

print(fildata1)        


users = [100,20,40,50,44,56,78,99]

while len(users)>0:
    x = users.pop()
    print(x)
        


 