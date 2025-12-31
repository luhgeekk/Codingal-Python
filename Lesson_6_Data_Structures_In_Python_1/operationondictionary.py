mydict = {"name":"Minal" , "age":16}

print(mydict["name"])
print(mydict.get("age"))

mydict["age"] = 17
print(mydict) 

mydict["fav food"] = "Pizza"
print(mydict)

mydict.pop("age")
print(mydict)

print("fav food:" , mydict.get("fav food"))
