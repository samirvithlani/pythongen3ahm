from multipledispatch import dispatch

class Amazone:

    @dispatch()    
    def search(self):
        print("search() method")
    
    @dispatch(int)
    def search(self,price):
        print("search(int) method")
    
    @dispatch(int,int)
    def search(self,price,discount):
        print("search(int,int) method")
    
    @dispatch(str,str)
    def search(self,product,category):
        print("search(string,string) method")



a = Amazone()
a.search("mobile","electronics")                       