#{1:1,2:4,3:9,4:16,5:25,6:36,7:49,8:64,9:81,10:100}
data = {i: i ** 2 if i %2 ==0 else i **3 for i in range(1,11)}
print(data)



data  ={i:i**3 if i %2 !=0 else i for i in range(1,11)}