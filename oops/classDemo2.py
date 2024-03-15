class Bank:
    
    ifscCODE = "HDFC0001234" # class variable # static variable
    
    def bankDetail(self): #b --> b.name = "HDFC Bank"
        self.name = "HDFC Bank" # instance variable
        balance = 10000 # local variable
        print("Bank Name is ",self.name)
        print("Bank Balance is ",balance)
        print("IFSC Code is ",Bank.ifscCODE)
    
    def userDetail(self): #b --> b.name = "HDFC Bank"
        print("bank name =  ",self.name)



b = Bank()
b.bankDetail()        
b.userDetail()