class Temperature:
    def __init__(self):
        self.day = 0
        self.temperature = 0
    @property
    def getDay(self):
        return self.day
    def setDay(self,d1):
        if d1>= 1:
            self.day = d1
        else:
            self.day = 1
    @property
    def get_temperature(self):
        return self.temperature
    def set_temperature(self,d2):
        self.temperature = d2
    def __del__(self):
        print("Temperature has been deleted")
    def show(self):
        print(" the temperature is :",self.temperature)
    def feel(self):

            if self.temperature <= -20 and self.temperature <= 0:
                print("day ",self.day,"Very cold")
            elif self.temperature <= 0 and self.temperature <= 10:
                print("day ",self.day,"cold")
            elif self.temperature >= 10 and self.temperature <= 20:
                print("day ",self.day,"average")
            elif self.temperature >= 20 and self.temperature <= 30:
                print("day ",self.day,"hot")
            elif self.temperature >= 30 and self.temperature <= 40:
                print("day ",self.day,"Very hot")
            else:
                print("Wrong")
d1 = Temperature()
day = int(input("Enter Day"))
temperature = int(input("Enter Temperature"))
d1.setDay(day)
d1.set_temperature(temperature)
print(d1.getDay)
print(d1.get_temperature)
d1.show()
d1.feel()