# 여행사 : 가나 여행사
# 홍 길동님이 내일 프랑스 여행을 갑니다.
# 박 영희님이 모레 이탈리아 여행을 갑니다.
class Travel:
    com = '가나'
    def __init__(self,name,firstname):
        self.name = name
        self.firstname = firstname

    def travel(self,day,country):
        msg = self.firstname+self.name+'이 '+day+' '+country+' 여행을 갑니다.'
        return msg


class Account:
    bank = 'KB'

    def __init__(self, name):
        self.name = name
        self.accno = ''

    def accInfo(self, accno):
        self.accno = accno

    def showInfo(self):
        return self.accno

print(f'{Travel.com} 여행사')
hong = Travel('길동','홍')
print(hong.travel('내일','프랑스'))
park = Travel('영희','박')
print(park.travel('모레','이탈리아'))

soo = Account('철수')
hee = Account('영희')
soo.accInfo('143-09-45677')
hee.accInfo('154-09-43059')
print(f'{soo.name} {Account.bank} {soo.showInfo()}')
print(f'{hee.name} {Account.bank} {hee.showInfo()}')