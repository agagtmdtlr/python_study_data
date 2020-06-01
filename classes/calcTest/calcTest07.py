class Dog:
    type = '치와와' # 클래스 변수

    def __init__(self,name):
        # self.name : 인스턴스 변수
        # name : 지역 변수
        self.name = name

chiwadol = Dog('치와돌')

print(chiwadol.type)
print(chiwadol.name)

chiwasoon = Dog('치와순')

print(chiwasoon.type)
print(chiwasoon.name)

print(Dog.type)
# print(Dog.name) # AttributeError: type object 'Dog' has no attribute 'name'