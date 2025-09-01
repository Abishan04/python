'''
d = {
    "name":"abishan",
    "age":20,
    "gender":"male"
    }
print(d)
print(type(d))
'''

data = [("name","Abi"),("age",20),("gender","male")]
d = dict(data)
print(d)
print(d["name"])

print(d.get("city","jaffna"))
d["Age"] = 20
d.update({'city':'jaffna'})
print(d)

d["nic"] = "200518600093"
print("name" in d)
del d["age"]
print(d)

d.pop("nic")
print(d)

d.popitem()#remove last item
print(d)



key = d.keys()
print(key)
value = d.values()
print(value)
key = d.keys()
print(key)
items = d.items()
print(items)

for key in d.keys():
    print(key,d[key])

for value in d.values():
    print(value)
    
for key,value in d.items():
    print(key,value)