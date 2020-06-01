count = int(input('판매 가능한 커피 잔량 : '))
price = int(input('단가 : '))

while True:
    coin = int(input('돈을 넣어 주세요 : '))
    if coin >= price:
        count -= 1
        print(f'거스름돈 : {coin-price} , 커피 잔량{count}')
    else :
        print('돈이 부족하니 돌려줍니다.')
    if count == 0:
        print('재고소진')
        break