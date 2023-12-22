# def checkRole(**kwargs):
#     if kwargs["role"]=="admin":
#         return kwargs
#     else:
#         return None


# x = checkRole(role="admin1",name="ram",email="ram@gmail.com")    
# print(x)


def checkRole(**kwargs):
    
    #return {i:j for i,j in kwargs.items() if i=="role" and j=="admin"}
    #return {i :j if  j=="admin" else None for i,j in kwargs.items()}
    return kwargs if kwargs["role"]=="admin" else None

print(checkRole(role="admin1",name="ram",email="ram@gmail.com"))