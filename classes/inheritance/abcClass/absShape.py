from abc import *
import math

class Shape(metaclass=ABCMeta):

    @abstractmethod
    def calcArea(self):
        pass

    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,heigth,linecr,incr):
        self.width = width
        self.height = heigth
        self.calcArea(width,heigth)
        self.draw(linecr,incr)

    def calcArea(self,width,heigth):
        self.area = width*heigth
    def draw(self,linecr,incr):
        self.linecr = linecr
        self.incr = incr

    def showInfo(self):
        print(f'너비 : {self.width}, 높이 : {self.height}\n'
              f'사각형 면적 : {self.area}\n'
              f'라인 색상 : {self.linecr}\n'
              f'채우기 색상 : {self.incr}')

class Circle(Shape):
    def __init__(self, radius, xpos,ypos, linecr, incr):
        self.radius = radius
        self.xpos = xpos
        self.ypos = ypos
        self.calcArea(radius)
        self.draw(linecr, incr)

    def calcArea(self, radius):
        self.area = pow(radius,2)*math.pi

    def draw(self, linecr, incr):
        self.linecr = linecr
        self.incr = incr

    def showInfo(self):
        print(f'반지름 : {self.radius}, 중심 : ({self.xpos},{self.ypos})\n'
              f'사각형 면적 : {self.area:.1f}\n'
              f'라인 색상 : {self.linecr}\n'
              f'채우기 색상 : {self.incr}')

mylist = [Rectangle(10,10,'red','green'),Circle(5,3,4,'pink','blue')]

for shape in mylist:
    shape.showInfo()
    print('-'*30)

print(Rectangle.mro())