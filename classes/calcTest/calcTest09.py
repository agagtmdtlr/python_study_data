class Television:
    channel = 100
    volume = 0
    wow = 0

    def __init__(self,name,volume):
        self.name = name
        self.volume = volume

    def showData(self):
        print('이름 :',self.name)
        print('채널 :',self.channel)
        print('볼륨 :',self.volume)

colortv = Television('컬러 티브이',10) # 볼륨
blacktv = Television('흑백 티브이',20)
colortv.showData()
blacktv.showData()

colortv.color = '파랑'
print('색상 :',colortv.color)

print(colortv.__dict__)
print(blacktv.__dict__)

print('원형 클래스 : ',Television,', 주소',id(Television))
print('컬러 : ',colortv,', 주소',id(colortv))
print('흑백 : ',blacktv,', 주소',id(blacktv))

Television.wow = 100
print(colortv.wow) # wow 속성을 클래스 변수를 참조하여 값을 불러온다.
colortv.wow = 100 # 속성을 생성하면 객체의 namespace로 할당된다.
Television.wow = 70 # 더이상 클래스 변수를 참조하지 않는다.
print(colortv.wow) # 클래스 변수가 아닌 객체 변수를 참조한다.
