teams= {"csk":["ms","jadeja","raina"],"rcb":["kohli","abd","siraj"]}
print(teams)

# teams["csk"].remove("raina")
# print(teams)

# teams["rcb"].append("sachin")
# print(teams)



for k,v in teams.items():
    print(k)
    print(v)
    for j in v:
        print(j)
    
    print("-----")    

