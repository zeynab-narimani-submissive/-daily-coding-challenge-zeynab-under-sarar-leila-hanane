class school:
    def __init__(self,name,family,AVG):
        self.name = name
        self.family = family
        self.AVG = AVG
    def maxAVG(self):
        maxi = max(self.AVG)
        for i in self.AVG:
            if i == maxi:
                j = self.AVG.index(i)
        print(self.name[j],self.family[j],self.AVG[j])
tplNames = ("Zhara","Mahsa","Nasrin","Zohre")
tplFamily = ("Razavi","Sadati","Miralami","Najafi")
tplAVG = (18,20,14,16)
s1 = school(tplNames,tplFamily,tplAVG)
s1.maxAVG() 