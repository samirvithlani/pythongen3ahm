
def data(*args,x):
    print(x)
    print(args)


data(10,20,30,40,50,x=100)    


def getData(**kwargs):
    print(kwargs)