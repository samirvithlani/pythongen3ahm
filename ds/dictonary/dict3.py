sales = {"iphone":1000, "ipad":2000, "macbook":3000}

#dict is iterable...

x = sales.get("iphone")
print(x)

#mutable...
print(sales)
sales["iphone"]=5000
print(sales)
sales["iphone 14"]=2000
print(sales)

sales.update({"iphone":10000,"imac":5000})

print(sales)