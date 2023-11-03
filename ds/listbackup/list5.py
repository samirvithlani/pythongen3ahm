nolist =[]
choice = -1

while True:
    
    no = int(input('Enter number: '))
    if str(no).endswith("456"):
        nolist.append(no)
    
    choice = int(input('Do you want to continue? 0-No, 1-Yes: '))
    if choice == 0:
        break

print(nolist)        
        