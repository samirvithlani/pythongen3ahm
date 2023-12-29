def average(a,b,c):
    if type(a) != int or type(b) != int or type(c) != int:
        return "Invalid Input"
    else:
        if a > 50 and b > 50 and c > 50:
            return (a + b + c) // 3
        else:
            return "Failed"



x = lambda a,b,c : average(a,b,c)

print(x(60,7,8))        
     