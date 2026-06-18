class human:
    def __init__(self,name,family,birthYear):
        self.name = name
        self.family = family
        self.birthYear = birthYear
    def age(self):
        return 2026 - self.birthYear
    def whoAmI(self):
        return "My name is " + self.name + " " + self.family + " and I am " + str(self.age())
class patient(human):
    def __init__(self,name,family,birthYear,doctorName):
        super().__init__(name,family,birthYear)
        self.dotorName = doctorName
    def doctorsName(self):
        return "patient name : " + self.name + " " + self.family + " \nDoctor name : " + self.dotorName
    def roomNumber(self,bedNumber):
        if bedNumber >= 1 and bedNumber <= 10:
            return self.name + " " + self.family + " is in room number 1"
        elif bedNumber >= 11 and bedNumber <= 20:
            return self.name + " " + self.family + " is in room number 2"
        elif bedNumber >= 21 and bedNumber <= 30:
            return self.name + " " + self.family + " is in room number 3"
        elif bedNumber >= 31 and bedNumber <= 40:
            return self.name + " " + self.family + " is in room number 4"
        else:
            return "Number of bed doesn't exist"
class teacher(human):
    def __init__(self,name,family,birthYear,subject):
        super().__init__(name,family,birthYear)
        self.subject = subject
    def subjectName(self):
        return self.name + " " + self.family + " teaches " + self.subject
    def condition(self,subject):
        if subject == "Programming":
            return "we need this teacher ."
        else:
            return "we do not need " + self.subject + " teacher"
n = input("Enter your name: ")
f = input("Enter your family: ")
b = int(input("Enter your birth year: "))
h1 = human(n,f,b)
print(h1.whoAmI())
d = input("Enter your Doctor's Name: ")
p1 = patient(n,f,b,d)
print(p1.doctorsName())
print(p1.roomNumber(25))
s = input("Enter your subject: ")
t1 = teacher(n,f,b,s)
print(t1.subjectName())
print(t1.condition(s))
print(t1.name)