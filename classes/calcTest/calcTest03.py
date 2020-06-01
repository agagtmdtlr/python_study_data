# 속성 : 이름, 값
# 동작 : 계산한다.(calc)

# 클래스 정의
# classes 클래스이름[(수퍼클래스 이름)]:
#     변수1
#     변수2 ...
#     def __init__(self,매개변수01,매개변수02,...)
#         여기는 생성자 파트 ...
#     함수 def 함수이름(self,매개변수01,매개변수02,...):
#         할일 ...

# 객체생성
# 객체이름 = 클래스이름(매개변수01,매개변수02, ...)

class Calculator :

    def __init__(self,name):
        self.name = name
        print(self.name+' 생성자 호출됨')
        self.result = 0
    def calc(self,num):
        self.result += num
        print('%d를 더합니다.' %(num))
        return self.result


soo = Calculator('철수')
print(soo.calc(3))
print(soo.calc(4))
print('-'*20)

hee = Calculator('영희')
print(hee.calc(5))
print(hee.calc(6))
print('-'*20)