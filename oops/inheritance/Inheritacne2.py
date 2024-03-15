class ChatGPT():
    
    company = "OpenAI"
    version = "GPT-3"
    
    def __init__(self):
        print("ChatGPT object is created")
        self.boatName = "GPT-3"


class Gemni():
    
    company = "Google"        
    
    def __init__(self):
        print("Gemni object is created")
        self.boatName = "Gemni"



class User(Gemni,ChatGPT):
    
    def __init__(self):
        super().__init__()
        print("User object is created")
        print("Company: ", self.company)
        print("comp",ChatGPT.company)
        print("Version: ", self.version)


u = User()                