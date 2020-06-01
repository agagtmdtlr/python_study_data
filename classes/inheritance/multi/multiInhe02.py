class Person:
    data = '사람 데이터'

    def greeting(self):
        print('안녕하세요')

    def skill(self):
        print('연설을 잘함')

    def eat(self):
        print('라면을 먹습니다.')
# end class Person


class University:

    def manage_credit(self):
        print('학점 관리')

    def skill(self):
        print('노래를 잘 함')

    def hobby(self):
        print('영화 감상')
# end class University


class Student(Person,University):
    def __init__(self):
        pass

    def study(self):
        print('공부하기')
# end class Student


class Graduates(University,Person):
    data = '졸업생 데이터'
    def __init__(self):
        pass

    def play(self):
        print('졸업생 고유메소드')

    def hobby(self): # 오버라이딩
        print('졸업생 오버라이딩')

    def showHobby(self):
        super().hobby()

    def showData(self):
        print(super().data)
# end class Graduates


soo = Student()
print(soo.data)
soo.greeting()
soo.skill()
soo.eat()
soo.study()
soo.manage_credit()
soo.hobby()
print('-'*30)
hee = Graduates()
print(hee.data)
hee.greeting()
hee.skill()
hee.eat()
hee.play()
print('-'*30)
print(hee.data)
hee.hobby()
print('-'*30)
hee.showHobby()
hee.showData()


print('finished')