class User:
    
    @staticmethod
    def getUserData():
        print("User Data")
    
    @classmethod
    def printUserData(self):
        print("User Data..")    



User.getUserData() #User Data        
u = User()
u.getUserData() 
u.printUserData() #User Data
User.printUserData() #User Data..
        