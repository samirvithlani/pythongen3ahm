def getUserData(users):
    
    for k,v in users.items():
        print(k,"=>",v)

getUserData({"name":"ram","age":20,"address":"mg road"})    


def getUserData1(users):
    k = users.keys()
    for i in k:
        if i == "name":
            print("true")
        else:
            print("false")    

#home work


getUserData1({"name":"ram","age":20,"address":"mg road"})