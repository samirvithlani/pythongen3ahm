email = "raj@gmail.comrr"
print(email)
print(len(email))

# email = email.strip('r')
# print(email)
# print(len(email))

email = email.rstrip("rr")
print(email)
print(len(email))

x =  email.startswith("r")
print(x)
x = email.endswith(".co")
print(x)
