class PhoneBook:
    myDict = {"Mahnaz barzegar":"0903516133","Nasim taheri":"09135426145","Arezo Sadati":"09135462843"}
a1 = PhoneBook()
#print(a1.myDict)
#print(a1.myDict["Arezo Sadati"])
#a1.myDict["Solmaz olomi"] = "091452467967"
#print(a1.myDict)
#a1.myDict["Nasim taheri"] = "0"
#print(a1.myDict)
del a1.myDict["Arezo Sadati"]
print(a1.myDict)
print(a1.myDict.keys())
print(a1.myDict.values())