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
            if self.temperature[i] >= -20 and self.temperature[i] <= 0:
                print("day ",i+1,"Very cold")
            elif self.temperature[i] >= 0 and self.temperature[i] <= 10:
                print("day ",i+1,"cold")
            elif self.temperature[i] >= 10 and self.temperature[i] <= 20:
                print("day ",i+1,"average")
            elif self.temperature[i] >= 20 and self.temperature[i] <= 30:
                print("day ",i+1,"hot")
            elif self.temperature[i] >= 30 and self.temperature[i] <= 40:
                print("day ",i+1,"Very hot")
            else:
                print("Wrong")
    def upperthan18(self):
        count18 = 0
        for i in self.temperature:
            if i>18:
                count18 +=1
        return count18
    def lowerthanzero(self):
        countlzero = 0
        for i in self.temperature:
            if i<0:
                countlzero += 1
        return countlzero
    def cmpyears(self,a):
        equal = 0
        colder = 0
        hotter = 0
        for i in range(len(self.temperature)):
            if a[i] == self.temperature[i]:
                equal += 1
            elif a[i] > self.temperature[i]:
                colder += 1
            else:
                hotter += 1
        print("Equal: ",equal,"colder: ",colder,"hotter: ",hotter)
    def cmpyearslistday(self,a):
        equal = []
        colder = []
        hotter = []
        for i in range(len(self.temperature)):
            if a[i] == self.temperature[i]:
                equal.append(i+1)
            elif a[i] > self.temperature[i]:
                colder.append(i+1)
            else:
                hotter.append(i+1)
        print("Equal: ",equal,"colder: ",colder,"hotter: ",hotter)
    def cmpyearslist(self,a):
        equal = []
        colder = []
        hotter = []
        for i in range(len(self.temperature)):
            if a[i] == self.temperature[i]:
                equal.append(self.temperature[i])
            elif a[i] > self.temperature[i]:
                colder.append(self.temperature[i])
            else:
                hotter.append(self.temperature[i])
        print("Equal: ",equal,"colder: ",colder,"hotter: ",hotter)
temperature0 = [22,20,14,9,-2,-10,5]
d1 = Temperature(temperature0)
d1.feel()
x = d1.upperthan18()
print("Upper than 18 :",x)
y = d1.lowerthanzero()
print("Lower than zero: ",y)
temperature1 = [25,20,15,7,-3,-1,-5]
d1.cmpyears(temperature1)
d1.cmpyearslist(temperature1)
d1.cmpyearslistday(temperature1)