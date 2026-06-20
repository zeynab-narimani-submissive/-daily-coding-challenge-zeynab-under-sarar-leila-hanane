class human:
    def __init__(self,name,family,gender,birthYear):
        self.name = name
        self.family = family
        self.gender = gender
        self.birthYear = birthYear
    def age(self):
        return 2026 - self.birthYear
    def whoAmI(self):
        return "My name is " + self.name + " " + self.family + " and I am " + str(self.age())
    def areYouOldEnough(self,age1):
        if age1 >= 18:
            return "You are old enough."
        else:
            return "You are not old enough."

class doctor(human):
    def __init__(self,name,family,gender,birthYear,):
        super().__init__(name,family,gender,birthYear)
        
    def introduction(self):
        return "My name is " + self.name + " " + self.family + " and I am a doctor "
class dentist(doctor):
    def __init__(self,name,family,gender,birthYear):
        super().__init__(name,family,gender,birthYear)
    def introduction(self):
        return "My name is " + self.name + " " + self.family + " and I am a dentist "

name = input("Enter your name: ")
family = input("Enter yor=ur family: ")
gender = input("Enter your gender F for female M for male: ")
date = input("Enter your birth year")
d1 = dentist(name,family,gender,date)
print(d1.introduction())