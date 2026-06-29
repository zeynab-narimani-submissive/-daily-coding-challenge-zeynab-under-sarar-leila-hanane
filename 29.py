class Computer:
    def __init__(self):
        self.maxprice = 900
    def sell(self):
        print("Selling Price Computer:",self.maxprice)
    def setMaxPrice(self, price):
        self.maxprice = price
class laptop:
    def __init__(self):
        self.maxprice = 800
    def sell(self):
        print("Selling Price laptop:",self.maxprice)
    def setMaxPrice(self, price):
        self.maxprice = price
c = Computer()
c.sell()
c.setMaxPrice(1000)
c.sell()
l=laptop()
l.sell()
l.setMaxPrice(900)
l.sell()