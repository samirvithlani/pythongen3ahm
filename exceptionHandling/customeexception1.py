class InvalidAgeException(Exception):
    
    def __init__(self,msg):
        super().__init__(msg)


age = int(input("Enter your age: "))

try:
    if age<18:
        raise InvalidAgeException("You are not allowed to enter this site")

except InvalidAgeException as e:
    print(e)            
    