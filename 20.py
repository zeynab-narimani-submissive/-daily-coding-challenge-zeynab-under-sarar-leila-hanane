class school:
    def __init__(self,studentName,studentClass,studentAverage):
        self.tplStudentName = studentName
        self.tplStudentClass = studentClass
        self.tplStudentAverage = studentAverage
    def printName(self):
        for i in range(len(self.tplStudentName)):
            print("#",i+1,"=",self.tplStudentName[i])
    def printClass(self):        
        for i in range(len(self.tplStudentClass)):
            print(self.tplStudentName[i],"Class=",self.tplStudentClass[i])
    def printStudentAVG(self):
        for i in range(len(self.tplStudentAverage)):
            print(self.tplStudentName[i],"AVG=",self.tplStudentAverage[i])
    def class1(self):
        lst1 = []
        for i in range(len(self.tplStudentClass)):
            if self.tplStudentClass[i] == 1:
                lst1.append(self.tplStudentName[i])
        return lst1
    def class2(self):
        lst2 = []
        for i in range(len(self.tplStudentClass)):
            if self.tplStudentClass[i] == 2:
                lst2.append(self.tplStudentName[i])
        return lst2
    def class3(self):
        lst3 = []
        for i in range(len(self.tplStudentClass)):
            if self.tplStudentClass[i] == 3:
                lst3.append(self.tplStudentName[i])
        return lst3
    def MAXAVG(self):
        maxAvg = self.tplStudentAverage[0]
        j= 0
        for i in range(1,len(self.tplStudentAverage)):
            if self.tplStudentAverage[i] > maxAvg:
                maxAvg = self.tplStudentAverage[i]
                j = i
        print("Max average = ",self.tplStudentName[j],",Average = ",maxAvg,"Class =",self.tplStudentClass[j])
    def MINAVG(self):
        minAvg = self.tplStudentAverage[0]
        j= 0
        for i in range(1,len(self.tplStudentAverage)):
            if self.tplStudentAverage[i] < minAvg:
                minAvg = self.tplStudentAverage[i]
                j = i
        print("Min average = ",self.tplStudentName[j],",Average = ",minAvg,"Class =",self.tplStudentClass[j])
    def sumAVG(self):
        sum = 0
        for i in range(len(self.tplStudentAverage)):
            sum += self.tplStudentAverage[i]
        print("Sum of average = ",sum)
    def avgAVG(self):
        sum = 0
        for i in range(len(self.tplStudentAverage)):
            sum += self.tplStudentAverage[i]
        print("Average of average = ",sum/len(self.tplStudentAverage))
    def subMaxAVG(self):
        lstMax = []
        m1 = max(self.tplStudentAverage)
        for i in self.tplStudentAverage:
            lstMax.append(m1-i)
        return lstMax
    def subMinAVG(self):
        lstMin = []
        m2 = min(self.tplStudentAverage)
        for i in self.tplStudentAverage:
            lstMin.append(i-m2)
        return lstMin
    def ave10to12(self):
        lstName1 = []
        for i in self.tplStudentAverage:
            if i >= 10 and i <= 12:
                j = self.tplStudentAverage.index(i)
                lstName1.append(self.tplStudentName[j])
        return lstName1
tplNames = ("Zhara Razavi","Mahsa Sadati","Nasrin Miralami","Zohre Najafi")
tplClass = (2,3,2,1)
tplAverage = (16.12,10.32,14.28,19.50)
s1 = school(tplNames,tplClass,tplAverage)
s1.printName()
print("********************")
s1.printClass()
print("********************")
s1.printStudentAVG()
print("class1",s1.class1())
print("class2",s1.class2())
print("class3",s1.class3())
s1.MAXAVG()
s1.MINAVG()
s1.sumAVG()
s1.avgAVG()
print(s1.subMaxAVG())
print(s1.subMinAVG())
print("Average 10 to 12: ",s1.ave10to12())