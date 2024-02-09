def checkStringAndReturnit(name):
    if type(name) == str:
        if len(name) < 3:
            return name.upper()
        else:
            return name.title()
    else:
        return "Invalid Input"    
    


#data = lambda name : checkStringAndReturnit(name)   
#data = lambda name,age : name if age > 18 else checkStringAndReturnit(name) 
data = lambda name : name if len(name)>3 else checkStringAndReturnit(name)
print(data(120)) 
      
      
      


