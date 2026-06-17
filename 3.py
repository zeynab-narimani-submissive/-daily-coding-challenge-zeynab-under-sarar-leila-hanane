class Temperature:
    def __init__(self,temperature):
        self.temperature = temperature
    def __del__(self):
        print("Temperature has been deleted")
    def show(self):
        #print(" the temperature is :",self.temperature)
        pass
    def feel(self):
        for i in range(len(self.temperature)):
            if self.temperature[i] <= -20 and self.temperature[i] <= 0:
                print("day ",i+1,"Very cold")
            elif self.temperature[i] <= 0 and self.temperature[i] <= 10:
                print("day ",i+1,"cold")
            elif self.temperature[i] >= 10 and self.temperature[i] <= 20:
                print("day ",i+1,"average")
            elif self.temperature[i] >= 20 and self.temperature[i] <= 30:
                print("day ",i+1,"hot")
            elif self.temperature[i] >= 30 and self.temperature[i] <= 40:
                print("day ",i+1,"Very hot")
            else:
                print("Wrong")
temperature0 = [-40,42,14,9,2,10,5]
o1 = Temperature(temperature0)
o1.show()
o1.feel()
temperature1 = [3,22,46,23,6,12,18,31]
o2 = Temperature(temperature1)
o2.show()
o2.feel()