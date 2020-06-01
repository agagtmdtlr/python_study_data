# 생성자
#   __init__
#   객체가 생성이 될 때, 호출이 되는 특수 함수/메소드
#소멸자 ( 자바는 JVM이 자동으로 소멸 시켜주니깐 걱정 댓츠 노노)
#   __del__
#   프로그램이 종료될 때, 자동으로 호출되는 특수 함수/메소드
#   주로, 마감 작업(파일 닫기,데이터베이스 접속 해지 등등)

class Information:
    def __init__(self,name):
        self.name = name
        print(self.name + ' 생성자가 호출되었습니다.')

    def __del__(self):
        print(self.name+' 소멸자')
        print('주로 마감 작업용으로 사용됩니다.')

    def add(self,a,b):
        result = a+b
        msg = f'{self.name}님 {a} + {b}는 {a+b}입니다!.'
        print(msg)

# kim = Information('김유신')
# kim.add(5,6)
# lee = Information('이순신')
# lee.add(3,4)

myobj = []
mylist = ['안중근','이봉창']
for saram in mylist:

    obj = Information(saram)
    myobj.append(obj)
    # del obj
print(obj.name)
print('끝')