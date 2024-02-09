def getData(*args,**kwargs):
    print("args is:",args)
    print("Type of args is:",type(args))
    print("kwargs is:",kwargs)
    print("Type of kwargs is:",type(kwargs))


getData(100,200,name="ram",age=25,city="pune")    