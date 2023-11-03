tech = ["java","python","c","cpp","node"]

print(tech)
#removedelm = tech.pop() #pop without index / param
removedelm = tech.pop(2) #pop with index / param

print("removing...",removedelm)
print(tech)


tech.remove("cpp")
print(tech)