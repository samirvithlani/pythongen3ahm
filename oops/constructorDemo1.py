#constructor is special method in python which can create using __init__(self)
#use of constructor is to initialize the instance variable
#type of constructor
#1. default constructor
#2. parameterized constructor
#when we create object of class then constructor is called automatically

class Book:
    
    def __init__(self):
        print("Book Object Created")
        self.name = "Python Programming"
        self.price = 500
        self.author = "abc"

    def getBookDetail(self):
        print(self.name)
        print(self.price)
        print(self.author)

b = Book() #constructor is called automatically  
b.getBookDetail()      