class BroadCast:
    def broadcast(self):
        print('방송합니다.')


class Kbs(BroadCast):
    def __init__(self,title,channel,time=None):
        self.title = title
        self.channel = channel
        self.time = time

    def broadcast(self):
        print(f'제목 : {self.title}\n'
              f'채널 : {self.channel}')
        if self.time:
            print(f'시간 : {self.time}')
        print('-' * 30)

    def hahahah(self):
        print('공영방송')
# end class Kbs


class Mbc(BroadCast):
    def __init__(self, title, channel, time=None):
        self.title = title
        self.channel = channel
        self.time = time

    def broadcast(self):
        msg = f'채널 {self.channel}번에서 {self.title}을(를) 방송합니다.'
        print(msg)
        print('-'*30)

    def hohoho(self):
        print('문화방송')
# end class Mbc


broad = BroadCast()
broad.broadcast()

syudol = Kbs('슈퍼맨이 돌아왔다.',7)
syudol.broadcast()

madang = Kbs('아침 마당',9,'오전 8시')
madang.broadcast()

mbc = Mbc('선을 넘는 녀석들',11)
mbc.broadcast()

# 메뉴 : 1입력시 Kbs , 2입력시 Mbc 객체를 생성
# obj 객체는 어떤 메뉴인가에 따라서 인스턴스 종류가 결정됩니다.
menu = int(input('메뉴를 입력하세요 : '))

if menu == 1 :
    title = input('제목 입력 : ')
    channel = int(input('채널 입력 : '))
    obj = Kbs(title,channel)
    obj.broadcast()
elif menu == 2 :
    title = input('제목 입력 : ')
    channel = int(input('채널 입력 : '))
    obj = Mbc(title, channel)
    obj.broadcast()
else:
    print('잘못 입력했습니다.')

if isinstance(obj,Kbs):
    obj.hahaha()
elif isinstance(obj,Mbc):
    obj.hohoho()

