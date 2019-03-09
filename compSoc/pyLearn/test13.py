#test 13

students = ["Bill", "Cory", "Dan", "Emily", "Fanny"]
grades = ["c", "B", "B", "D", "A"]

myDict = {}
myDict["Bill"] = "C"
myDict["Cory"] = "B"
myDict["Dan"] = "B"
myDict["Emily"] = "D"
myDict["Fanny"] = "A" 

print(myDict["Bill"])
print(myDict["Fanny"])

print("Is Kyle in my dictionary:")
print("Kyle" in myDict)

del(myDict["Fanny"])
print("Is Fanny in my dictionary:")
print("Fanny" in myDict)

print(myDict.keys())
print(myDict.values())
