class Animal :
    def __init__(self):
        self.speed = 10
    def move(self):
        print('수퍼 클래스의 move 함수')

class Dog(Animal) :
    def __init__(self,name):
        self.name = name
        super().__init__()
        print(super().__class__)

    def intoduce(self):
        print('나는 \'%s\'입니다.' % self.name)

class Cat(Animal) :
    pass

mydog = Dog('멍멍이')
mydog.move()

mycat = Cat()
mycat.move()