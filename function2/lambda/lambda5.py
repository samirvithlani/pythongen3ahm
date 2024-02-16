def isValid(name):
    if " " in name:
        return False



x = lambda name: isValid(name)    
print(x("John Doe")) # False