marks = [12,34,56,78,23,45,66]
print(marks)

#x = marks.pop()
x = marks.pop(2)
#print("removing........ ",x)
print(x)
print(marks)
if marks.count(788) > 0:
    marks.remove(78)
else:
    print("not found")    


cnt = marks.count(45)
print("count...",cnt)    


print(marks)






