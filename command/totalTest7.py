# whatChange.pyy
# '물건 가격'과 '받은 금액'을 입력 받아서,
# 얼마를 거슬러 줘야 하는 지 프로그램을 작성해 보세요.
# product,receive = map(int,
#                       input('물건가격,'
#                             '받은금액 : ').split(','))
product,receive = 15000,50000
give = receive-product
usegive = give
pay = [50000,10000,5000,1000,500,100,50,10,5,1]
count = []
for i in pay:
    temp = usegive//i
    count.append(temp)
    usegive -= i*temp
form = f'''물건 가격 : {product}
받은 금액 : {receive}
거스름 돈 : {give}

다음과 같이 거슬러 주세요\n'''
for i,v in enumerate(pay) :
    if count[i] is not 0 :
        form += f'{v} x {count[i]}장\n'
print(form)
# 출력 예시
# 물건 가격 : 15000
# 받은 금액 : 50000
# 거스름 돈 : 35000
#
# 다음과 같이 거슬러주세요:
# 10000 x 3장
# 5000 x 1장