import re

class PhoneBook:
    def __init__(self,n,d):
        self.name = n
        self.myDict = d
        print("a phone book has been created!")
    def own(self):
        print("The Owner of the Phone Book is: ", self.name)
    def searchKey(self,k):
        print(k,"=",self.myDict[k])
    def searchValue(self,v):
        for i,j in self.myDict.items():
            if v == j:
                print(i,"=",j)
    def findCity(self,code):
        for i, j in self.myDict.items():
            if code == j[0:4]:
                print(code,":",i)
    def findSadati(self):
        for i, j in self.myDict.items():
            if "Sadati" == i[-6:]:
                print("Sadati is",":",i)
    def __del__(self):
        print("The object has been deleted!")

myDict1 = {"Mahnaz barzegar":"0903516133","Nasim taheri":"09135426145","Arezo Sadati":"09135462843"}
a1 = PhoneBook("hana",myDict1)
a1.own()
a1.searchKey("Arezo Sadati")
a1.searchValue("0903516133")
myDict2 = {"Mahnaz barzegar": "0903516133", "Nasim Sadati": "09135426145", "Arezo Sadati": "09135462843","Fariba Gholami":"09125468721"}
a2 = PhoneBook("zoya",myDict2)
a2.own()
a2.findCity("0912")
a2.findSadati()