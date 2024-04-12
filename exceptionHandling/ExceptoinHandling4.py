from AllExcpetions import inValidException

name = input("Enter your name: ")

try:
    if len(name)<3:
        raise inValidException("Name should be more than 3 characters")
except inValidException as e:
    print(e)
        
