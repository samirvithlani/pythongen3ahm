
try:
    age = int(input("Enter your age: "))
except ValueError as e:
    print(e)
else:
    print("No exception occured")
    print("Age is: ",age)        


try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)
        