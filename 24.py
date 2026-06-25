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
    
w1 = warehouse()
w1.fill()