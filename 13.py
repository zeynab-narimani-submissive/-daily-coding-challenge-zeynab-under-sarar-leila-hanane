class municipalityـcars:
    def __init__(self,car_name,max_speed,number_of_chairs):
        self.car_name = car_name
        self.max_speed = max_speed
        self.number_of_chairs = number_of_chairs
    def searchByName(self,key):
        flag = False
        for i in range(len(self.car_name)):
            if self.car_name[i] == key:
                flag = True
                print(self.number_of_chairs[i])

        if flag == False:
            print("not found")
car_name = ["BMW","Mercedes","Audi"]
max_speed = [240,250,260]
number_of_chairs = [5,5,5]
m1 = municipalityـcars(car_name,max_speed,number_of_chairs)
m1.searchByName("BMW")