max = lambda a,b : a if a > b else b
print(max(10,20))

data = lambda name : name.upper() if len(name) >= 5 else name
print(data("pyt")) 


max = lambda a , b, c : a if a >b and a > c else b if b >c else c
print(max(10,200,30)) 


#name < 3 upper
#name > 3 and les > 5 title
#cap 
data1 = lambda name : name.upper() if len (name)< 3 else name.title() if len(name)>=5 and len(name)<=10 else name.capitalize() 

print(data1("python is a programming language"))
