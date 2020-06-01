jumsu = 80

def someFunction():
    print('모듈 내의 함수')

class Student:
    jumsu = 70
    def someFunction(self):
        print('클래스 내의 함수')
    def showInfo(self):
        #jumsu = 60
        # jumsu 변수는 지역 변수를 찾습니다.
        # 없으면 모듈의 변수를 찾습니다.
        print(self.jumsu) # 클래스 내의 멤버(인스턴스) 변수를 참조

        someFunction()
        self.someFunction()

soo = Student()
soo.showInfo()