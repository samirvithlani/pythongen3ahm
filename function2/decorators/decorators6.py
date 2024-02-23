data = {"id":1,"name":"ram","role":"manager","age":23}


def checkPermission(func):
    
    def inner(role): #manager
        if data["role"] == role:
            func(data) #accessDb(dict....)
        else:
            print("You don't have permission to access the data")
    
    return inner            


@checkPermission
def accessDb(data): #dict..
    print("accessDb accessed")
    print(data)


accessDb("user")    