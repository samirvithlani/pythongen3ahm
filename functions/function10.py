def getUserData(no,**kwargs):
    print(kwargs["name"])
    print(kwargs.get("name"))
    print(kwargs)
    print(no)
    print(type(kwargs))


getUserData(100,name="ram",email="ram@gmail.com")    