#overloading:
#search
#search()
#search(int)
#search(int,int)
#search(string,string)
#search(string,string,int)


class Amazone:
    
    def search(self):
        print("search() method")
    
    def search(self,price):
        print("search(int) method")
    
    def search(self,price,discount):
        print("search(int,int) method")
    
    def search(self,product,category):
        print("search(string,string) method")



a = Amazone()
a.search()                       