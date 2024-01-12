data = ["apple","orange","banana","grapes","mango","strawberry"]

data.append("kiwi")
print(data)

data.insert(2,"papaya")
print(data)


removedElm = data.pop() #it will remove last element
print("removing...",removedElm)
print(data)

removedElm = data.pop(3)
print("removing...",removedElm)
print(data)


#multi add....
#data.append(["watermelon","muskmelon","pomegranate"])
#data.extend(["watermelon","muskmelon","pomegranate"])
#data.extend(["watermelon"])
print(data)