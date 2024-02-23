role = input("Enter your role: ")


def checkAccess(func):
    
    def inner():
        print("Checking access")
        if role == "admin" or role =="manager":
            print("Access granted")
            func()
        else:
            print("Access denied")
    
    return inner


@checkAccess
def getUserData():
    print("User data is being processed")


getUserData()
            