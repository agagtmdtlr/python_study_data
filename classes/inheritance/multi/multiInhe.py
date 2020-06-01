from abc import ABCMeta
from abc import abstractmethod

# ABCMeta : 추상 메소드를 잘 구현하고 있는지 감시 역할
class Horse(metaclass=ABCMeta):
    @abstractmethod # decorator
    def run(self):
        pass
# end class Horse


class Bird(metaclass=ABCMeta):
    @abstractmethod # decorator
    def fly(self):
        pass
# end class Bird


class Unicon(Horse,Bird):
    def __init__(self,name,speed):
        print(Unicon.__mro__)
        self.name = name
        self.speed = speed

    def __del__(self):
        print(f'{self.name}이가 죽었습니다.')

    def run(self): # 구현화/구체화/implementation
        print(f'{self.name}이(가) 시속 {self.speed}으로 달립니다.')
    # end method run

    def fly(self):
        print(f'{self.name}이(가) 시속 {self.speed}으로 날아다닙니다.')
    # end method fly


# end class Unicon
unidol = Unicon('유니돌',30)
unidol.fly()
unidol.run()

print('finished')