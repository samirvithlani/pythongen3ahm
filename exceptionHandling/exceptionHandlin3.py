age = int(input("Enter your age: "))

try:
    if age<18:
        raise Exception("You are not allowed to enter this site")
except Exception as e:
    print(e)    