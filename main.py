import math
from abc import ABC, abstractmethod

# DEFINE THE CLASSES

class shape(ABC):
    @abstractmethod
    def getArea(self):
        pass

class square(shape):
    def __init__(self, l):
        self.length = l
    def getLength(self):
        return self.length
    def setLength(self,l):
        self.length = l
    def getArea(self):
        return self.length**2

class rectangle(square):
    def __init__(self,l,w):
        super().__init__(l)
        self.width = w
    def getWidth(self):
        return self.width
    def setWidth(self, w):
        self.width = w
    def getArea(self):
        return self.width*self.length

class circle(shape):
    def __init__(self,r):
        self.radius = r
    def getRadius(self):
        return(self.radius)
    def setRadius(self,r):
        self.radius = r
    def getArea(self):
        return math.pi*self.radius**2

class semi(circle):
    def getArea(self):
        return 0.5*math.pi*self.radius**2

class box:
    def __init__(self,objSquare, objRectangle, objCircle, objSemi):
        self.objectSquare = objSquare
        self.objectRectangle = objRectangle
        self.objectCircle = objCircle
        self.objectSemi = objSemi

    def printInfo(self,name):
        if name=="Square":
            print("The square has length of", self.objectSquare.getLength())
            print("The square has area of",self.objectSquare.getArea())
            print("--------------------------------------------------------------------")
        if name=="Rectangle":
            print("The rectangle has length and width of",self.objectRectangle.getLength()," and ",self.objectRectangle.getWidth())
            print("The rectangle has area of",self.objectRectangle.getArea())
            print("--------------------------------------------------------------------")
        if name=="Circle":
            print("The circle has radius of", self.objectCircle.getRadius())
            print("The circle has area of",self.objectCircle.getArea())
            print("--------------------------------------------------------------------")
        if name=="Semi":
            print("The semi (circle) has radius of", self.objectSemi.getRadius())
            print("The semi (circle) has area of",self.objectSemi.getArea())
            print("--------------------------------------------------------------------")

# CREATE 4 SHAPES
objSquare = square(2)
objRectangle = rectangle(3,4)
objCircle = circle(1)
objSemi = semi(2)

# CREATE A BOX TO HOLD THE 4 SHAPES
objBox = box(objSquare, objRectangle, objCircle, objSemi)

# PRINT INFO OF EACH SHAPE IN THE BOX
objBox.printInfo("Square")
objBox.printInfo("Rectangle")
objBox.printInfo("Circle")
objBox.printInfo("Semi")

# QUIT
quit()