try:
    no1 = int(input("Enter first number: "))
    no2 = int(input("Enter second number: "))
    print("no1 = ",no1)
    ans = no1/no2
    print("Answer = ",ans)
except ValueError:
    print("Please enter only numbers")  

except ZeroDivisionError:
    print("Please enter non-zero number for second number")    
    
except Exception:
    print("Some error occured")      