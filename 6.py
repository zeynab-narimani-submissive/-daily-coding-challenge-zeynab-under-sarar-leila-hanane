from importlib.resources import contents


class menu:
    def __init__(self,foodlist,pricelist):
        self.foodlist = foodlist
        self.pricelist = pricelist
    def __del__(self):
        print("This menu has been deleted")
    def addmenu(self,n):
        for i in self.foodlist:
            if i == n :
                return self.foodlist
        self.foodlist.append(n)
        return self.foodlist
    def delmenu(self,n):
        for i in self.foodlist:
            if i == n :
                self.foodlist.remove(n)
                return self.foodlist
        return "not found"
    def addprice(self):
        for i in range(len(self.foodlist)):
            print("Enter price of",self.foodlist[i],":",end="")
            n = int(input())
            self.pricelist.append(n)
        return self.pricelist
    def factor(self):
        foodcount = []
        for i in range(len(self.foodlist)):
            print("How many ",self.foodlist[i],"do you want?",end="")
            n = int(input())
            foodcount.append(n)
        print("**************************")
        print("name     count       price       total")
        sum = 0
        for i in range(len(self.foodlist)):
            print(self.foodlist[i],"     ",foodcount[i],"       ",self.pricelist[i],"       ",self.pricelist[i]*foodcount[i])
            sum+=self.pricelist[i]*foodcount[i]
        print("**************************")
        print("Total : ",sum)

    def foodContent(self):
        foodKeys = dict.fromkeys(self.foodlist,"")
        for i in food_list:
            print("What is content of ",i,": (if you want to finish press n")
            content = ""
            contentList = []
            while content != "n":
                contentList.append(content)
                content = input()
            foodKeys[i] = contentList[1:]
        return foodKeys
    def allergy(self,foodKeys,allergyTo):
        for i,j in foodKeys.items():
            for k in j:
                if allergyTo == k:
                    print(i,"have",allergyTo)
food_list = ["pasta","pizza","french fries","lasania"]
price_list = []
m1 = menu(food_list,price_list)
#n = input("Enter name of food to add")
#print(m1.addmenu(n))
#n = input("Enter name of food to remove")
#print(m1.delmenu(n))
#m = m1.addprice()
#print(m)
d1= m1.foodContent()
#m1.factor()
m1.allergy(d1,'a')