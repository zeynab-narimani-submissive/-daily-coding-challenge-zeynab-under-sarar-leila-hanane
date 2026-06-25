class warehouse:
    def __init__(self):
        self.name = []
        self.count = []
        self.kind = []
        self.price = []
    def __del__(self):
        print("warehouse has been deleted")
w1 = warehouse
w1.__del__