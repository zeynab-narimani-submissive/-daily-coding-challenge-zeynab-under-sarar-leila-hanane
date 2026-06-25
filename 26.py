class warehouse:
    def __init__(self):
        self.name = []
        self.count = []
        self.kind = []
        self.price = []
    def fill(self):
        while True:
            self.name.append(input("Enter a name:"))
            self.count.append(int(input("Enter a count number:")))
            self.kind.append(input("Enter kind of the product:"))
            self.price.append(float(input("Enter price of product:")))

            answer = input("do you want to continue?(y/n)")
            if answer == "n":
                break
        print(self.name)
        print(self.count) 
        print(self.kind) 
        print(self.price)
    def factor(self):
        lstN = []
        lstC = []
        lstP = []
        while True:
            b=input("What do you want to buy?\n")
            c=int(input("How many?\n"))
            m=self.name.index(b)
            self.count[m]-=c
            lstN.append(b)
            lstC.append(c)
            lstP.append(c*self.price[m])
            answer = input("do you want to continue?(y/n)")
            if answer == "n":
                break
        print("****factor****")
        print("name:",lstN)
        print("count:",lstC) 
        print("price:",lstP) 
        print("sum",sum(lstP))
        print("****factor****")
    def searchMaxPrice(self):
        maxPrice = max(self.price)
        indexMaxPrice = self.price.index(maxPrice)
        print("The product with the highest price is:")
        print("Name:", self.name[indexMaxPrice])
        print("Count:", self.count[indexMaxPrice])
        print("Kind:", self.kind[indexMaxPrice])
        print("Price:", self.price[indexMaxPrice])
    def searchKind(self, kind):
        indices = [i for i, k in enumerate(self.kind) if k == kind]
        if indices:
            print(f"Products of kind '{kind}':")
            for i in indices:
                print("Name:", self.name[i])
                print("Count:", self.count[i])
                print("Price:", self.price[i])
                print("---")
        else:
            print(f"No products found of kind '{kind}'.")
w1 = warehouse()
w1.fill()
w1.factor()
w1.searchMaxPrice()
w1.searchKind("underwear")  # Example kind to search for