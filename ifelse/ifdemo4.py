# cond 1 and cond 2
# T T -> T
# F - -> F
# T F -> F
# cond1 or cond 2
# T - -> T
# F T -> T
# F F -> F

isAlive = True
isRetired = True
savings =60000


# if isAlive == True and isRetired == False:
#     print("You are working")
#if savings>=5000000 or (isAlive == True and isRetired ==True):
if isAlive ==True and (isRetired == True or savings>=5000000):
    print("You are retired | ekdum mast")   
else:
    print("You are dead")    






