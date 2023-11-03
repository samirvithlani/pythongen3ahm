sales = [[10,20],[10,15],[8,7],[5,5],[5,5],[20,30],[10,50]]
salestotal =[]

total = 0
for i in range(len(sales)):
    total = 0
    for j in range(len(sales[i])):
        total = total + sales[i][j]
    
    salestotal.append(total)    
    

print(salestotal)    

m = max(salestotal)
print(m)
        
    