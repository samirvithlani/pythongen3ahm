class Google:
    country = "USA"
    def __init__(self):
        self.cname = "Google"
        self.cheadquarter = "Mountain View, California, United States"
    
    def getGoogle(self):
        print("Name: ", self.cname)
        print("Headquarter: ", self.cheadquarter)    


class Android(Google):
    
    def __init__(self):
        super().__init__()
        self.name = "Android"
        self.version = "Android 10"
        
    def getAndroid(self):
        self.getGoogle()
        print("Country: ", self.country)
        print("Name: ", self.cname)
        print("Headquarter: ", self.cheadquarter)
        print("Product: ", self.name)
        print("Version: ", self.version)            
        

a = Android()
a.getAndroid()        