data = [10,20,50,60]
try:
    data.remove(20)
except ValueError as e:
    print(e)   

finally:
    print("Finally block is always executed")     
    data=[]