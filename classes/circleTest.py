import math as m

class Circle:
    getarea = lambda r : round(m.pow(r,2)*m.pi,1)
    def __init__(self,x,y,r):
        self.position = (x,y)
        self.radius = r
        self.area = Circle.getarea(r)

    def showData(self):
        msg = f'원 중심 : {self.position}\n' \
              f'반 지름 : {self.radius}\n' \
              f'면적 : {self.area:}'
        print(msg)


circle01 = Circle(3,5,10)
circle01.showData()