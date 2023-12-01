sales = {"iphone":1000, "ipad":2000, "macbook":3000,"ipod":4000,"imac":5000}

print(sales)
removedelm = sales.pop("ipad")
print("removing,....",removedelm)
print(sales)


remv = sales.popitem()
print("removing,....",remv)
print(sales)