def checkStringAndReturnit(name):
    if type(name) == str:
        if len(name) < 3:
            return name.upper()
        else:
            return name.title()
    else:
        return "Invalid Input"    
    


data = lambda name : checkStringAndReturnit(name)   
print(data(120)) 
        