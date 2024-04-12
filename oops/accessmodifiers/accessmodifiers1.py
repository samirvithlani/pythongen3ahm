class Bank:
    __bankbal = 100
    _bankName = "SBI"
    
    
    def __init__(self):
        print("Bank class object created")
        print("Bank Balance: ", Bank.__bankbal)
        print("Bank Name: ", Bank._bankName)
        self.__accountbal = 1000
        
    def display(self):
        print("Bank Balance: ", Bank.__bankbal)
        print("Bank Name: ", Bank._bankName)


class SBI(Bank):
    def __init__(self):
        print("SBI class object created")
        print("Bank Balance: ",self.Bank__bankbal)
        
        
b = Bank()
b.display()

#print("Bank Balance: ", b.__bankbal)
#print("Bank Name: ", b._bankName)            
print("Bank Balance: ", b.__accountbal) #AttributeError: 'Bank' object has no attribute '__accountbal'

#s = SBI()
    
    