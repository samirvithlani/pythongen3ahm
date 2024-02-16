data = [10,23,43,22,67,89]


evenList = list(filter(lambda x: x%2==0,data))
print(evenList)

users = ["ram","racecar","madam","shyam","sharma"]

palidomre = list(filter(lambda x: x==x[::-1],users))
print(palidomre)
