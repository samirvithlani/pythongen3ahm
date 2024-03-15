class Library:
    
    def __init__(self,city): #l1 - city = "Pune"
        print("Library Object Created")
        self.name = "Central Library"
        self.city = city #copy the value of city to instance variable
        self.getLibraryData()
    
    
    def getLibraryData(self): #l2
        print(self.name)
        print(self.city)


l1 = Library("Pune") #constructor is called automatically
l1.getLibraryData()            


l2 = Library("Mumbai") #constructor is called automatically
l2.getLibraryData()