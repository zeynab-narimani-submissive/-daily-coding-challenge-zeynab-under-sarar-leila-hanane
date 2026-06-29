class Polygon:
    def namePolygon(self):
        print("it is Polygon")
    def propertyPolygon(self):
        print("I have area and circumference ")

class Square(Polygon):
    def nameSquare(self):
        print("it is Square")
    def areaSquare(self,side):
        print(side*side)
    def circumferenceSquare(self,side):
        print(side*4)

class Circle(Polygon):
    def nameCircle(self):
        print("it is Circle")
    def areaCircle(self,Radius):
        print(Radius*Radius*3.14)
    def circumferenceCircle(self,Radius):
        print(Radius*2*3.14)
    

s1 = Square()
s1.nameSquare()
s1.areaSquare(3)
s1.circumferenceSquare(3)
c1 = Circle()
c1.nameCircle()
c1.areaCircle(2)
c1.circumferenceCircle(2)