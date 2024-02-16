#annonimous function
def test():
    print("Hello froom test function")

test()
t = lambda :print("Hello from lambda function")
t()

def sum(a,b):
    print(a+b)

sum(10,20)    


x = lambda a,b : print(a+b)
x(100,20)

def average(a,b,c):
    return (a+b+c)//3

ans = average(10,20,30)
print("average...",ans)


avg = lambda a,b,c : (a+b+c)//3

print("average...",avg(10,20,300))







    

