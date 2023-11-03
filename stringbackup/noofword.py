# name = input("enter the name: ")
# count=0
# for i in name:
#     if i == "i":
#         count+=1

# print("no of words",count)        



# data = input("enter data")
# ch = input("enter the character")
# ind = -1
# #java -4 
# # 4
# #0 1 2 3
# for i in range(0,len(data)):
#     # data[0] == "j"
#     # data[1] == "a"
#     if data[i] == ch:
#         #ind =1
#         ind = i
#         break

# print("index of",ch,"is",ind)    
        

# name = input("enter the name: ")

# print(name.isalpha())
    



# x = name.isalpha()        
# if x ==True:
#     print("valid name")
# else:
#     print("invalid name")    
    


# name = input("enter the name: ")
# name = name.strip()
# if name.startswith("a") and len(name)>3:
#     print("valid name")

# else:
#     print("invalid name")        
    

# name = input("enter the name: ")
# temp = name[::-1]
# print(temp)

# if name == temp:
#     print("palindrome")

# else:
#     print("not palindrome")    
    

fname = input("enter the first name: ")

data = fname.split(" ")
print(data)
maxvar = data[0]
#hi welcome to python
#maxvar = hi
#print(max(data))    

for i in range(0,len(data)):
    # len(hi)<len(hi)
    # len(hi)<len(welcome)
    # len(welcome)<len(python)
    if len(maxvar)<len(data[i]):
        #maxvar = welcome
        maxvar = data[i]

print("longest word is",maxvar)        







    