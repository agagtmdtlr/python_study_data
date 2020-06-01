class Point:
    def __init__(self,xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos

    def showPoint(self):
        print(f'점의 좌표 : ({self.xpos},{self.ypos})')

class ColorPoint(Point):
    def __init__(self,xpos,ypos,color):
        super().__init__(xpos,ypos)
        self.color = color

    def showPoint(self):
        super().showPoint()
        print(f'색상 : {self.color}')

somedata = ColorPoint(5,6,'파랑')
mylist = [somedata,ColorPoint(7,8,'빨강')]

for i in mylist:
    i.showPoint()
    print('-'*20)