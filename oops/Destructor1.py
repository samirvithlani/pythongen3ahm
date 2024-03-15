class Bank:
    
    def __init__(self):
        print("Bank object is created")
    
    def __del__(self):
        print("Bank object is deleted")



b = Bank()       
del b     


