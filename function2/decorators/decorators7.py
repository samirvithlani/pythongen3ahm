def checkList(func):
    
    def inner(data):
        for i in data:
            if i == i[::-1]:
                func(True)
                break
            else:
                print("No palindrome found")
    
    return inner



@checkList
def myList(flag):
    print("flag is",flag)
    

myList(["ram","shyam","madam","radar","hello","world"])    
    
                