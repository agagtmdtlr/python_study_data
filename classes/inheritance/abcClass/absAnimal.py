from abc import ABCMeta
from abc import abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def move(self):
        pass

class Lion(Animal):
    def __init__(self,name,location):
        self.name = name
        self.loctaion = location

    def move(self):
        msg = f'{self.name}가(이) {self.loctaion}에서 달립니다.'
        print(msg)

class Eagel(Animal):
    def __init__(self,name,location):
        self.name = name
        self.loctaion = location

    def move(self):
        msg = f'{self.name}가(이) {self.loctaion}에서 납니다.'
        print(msg)


mylist = [Lion('사자','아프리카 초원'),Eagel('독수리','하늘')]

for ani in mylist:
    ani.move()