teams = {"csk":{"ms":"keeper","jadeja":"allrounder","raina":"batsman"},"rcb":{"kohli":"batsman","abd":"batsman","siraj":"bowler"}}
print(teams)

print("csk ..",teams["csk"])

for k,v in teams["csk"].items():
    print(k,"--",v)