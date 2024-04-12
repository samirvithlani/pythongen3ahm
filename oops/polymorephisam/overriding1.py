#overrding
#parent class's method creaeted in child class with same signature called method overriding
#access modifier should be same
#return type should be same
#method name should be same
#parameter should be same

class Parent:
    
    def show(self):
        print("Parent class show() method")


class Child(Parent):
    
    def show(self):
        super().show()
        print("Child class show() method")      


c = Child()
c.show() #Child class show() method          