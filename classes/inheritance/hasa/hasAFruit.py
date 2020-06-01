# 품목, 수량, 단가를 입력 받아서 10% 할인된 금액을 출력해주는 프로그램 작성
class Fruit: # 품목, 수량, 단가를 담고 있다.
    def __init__(self, item, qty, price):
        self.item = item
        self.qty = qty
        self.price = price

    def showInfo(self, idx):
        print(f'{idx}번째 품목 : {self.item}\n'
              f'수량 : {self.qty}\n'
              f'단가 : {self.price}')

        amount = (1 - 0.1) * self.qty * self.price
        print('판매 금액 : %.3f' %(amount))
# end class Fruit:

    def __del__(self):
        print('과일 사라진다 뿅!')


class Sales:
    def __init__(self, iter):
        totalsum = 0
        for idx in range(iter):
            # 과일의 정보 입력
            item = input('품목 입력 : ')
            try: # 정수 변환에 대한 format error 예외 처리
                qty = int(input('수량 입력 : '))
                price = int(input('단가 입력 : '))
            except Exception as err:
                print(err)
                qty = 0
                price = 0
            # 과일의 정보 입력
            self.fruit = Fruit(item, qty, price) # 과일 생성
            self.fruit.showInfo(idx+1) # 과일 생성됬는지 정보 확인
            totalsum += qty
        # end for
        print('총 판매 수량 : ',totalsum)
    # end method __init__()

iter = 2 # 상품 판매 건수
mysales = Sales(iter)