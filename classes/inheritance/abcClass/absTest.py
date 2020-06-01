from abc import ABCMeta
from abc import abstractmethod

class AbstractClass(metaclass=ABCMeta):
    @abstractmethod #데코레이터
    def move(self):
        pass

class NormalClass(AbstractClass):
    # 추상 메소드를 오버라이딩 하지 않았을 경우 에러
    # TypeError: Can't instantiate abstract class NormalClass
    # with abstract methods move
    def move(self):
        print('구현된 메소드 입니다.')

obj = NormalClass()
print('finished')
