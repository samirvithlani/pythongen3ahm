
#12456
#78456
#12345
#456
#1456
#3456

namelist =[]
choice =-1

while True:
    name  = input('Enter name: ')
    if len(name)>3:
        namelist.append(name)
    else:
        print('Name should be more than 3 characters')    
    
    choice = int(input('Do you want to continue? 0-No, 1-Yes: '))
    if choice == 0:
        break

print(namelist)    



# no = 123
# print(no)
# print(type(no))    


# strno = str(no)
# print(strno)
# print(type(strno))