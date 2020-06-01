class Dosirak:
    def __init__(self,name,price,*ar):
        self.name = name
        self.price = price
        self.ar = ar

    def showInfo(self):
        print(f'이름 : {self.name}\n'
              f'가격 : {self.price}\n'
              f'{"#".join(self.ar)}')

class Bag:
    def __init__(self):
        self.isOpened = False
        self.dosirak = []

    def open(self):
        self.isOpened = True
        print('도시락 가방 뚜껑 열기')

    def put(self,do):
        if self.isOpened == True:
            self.dosirak.append(do)
            print('도시락 가방에 도시락을 담음')
            do.showInfo()
        else :
            print('도시락 가방이 닫혀서 도시락을 넣을 수 없음')

    def close(self):
        self.isOpened = False
        print('도시락 가방 뚜껑 닫기')


mybag = Bag()

do01 = Dosirak('진달래도시락', 7000, '계란 후라이', '김', '마른 멸치')
mybag.put(do01)
mybag.open()
mybag.put(do01)
mybag.close()
print('-'*20)
do02 = Dosirak('매화도시락', 10000, '고급 어묵', '김치', '단호박 샐러드')
mybag.open()
mybag.put(do02)
mybag.close()