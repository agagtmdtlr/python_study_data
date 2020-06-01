class Point: # xpos,ypos를 가지고 있는 클래스
    def __init__(self,xpos,ypos):
        self.xpos = xpos
        self.ypos = ypos

    def move(self,xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
# end class Point:

class Circle: # radius(반지름)
    def __init__(self,radius, xpos, ypos):
        self.radius = radius
        self.pos = Point(xpos,ypos) # has a 관계

    def movePosition(self, xpos, ypos):  # 중심 이동
        self.pos.move(xpos, ypos)

    def display(self):
        msg = f'반지름 : {self.radius}\n' \
              f'중심 : {self.pos.xpos},{self.pos.ypos}'
        print(msg)




smallcircle = Circle(5,3,4)
smallcircle.display()
smallcircle.movePosition(1,1)
smallcircle.display()

largecircle = Circle(10,5,7)
largecircle.display()
largecircle.movePosition(-2,3)
largecircle.display()