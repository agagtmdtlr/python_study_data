# 급여를 입력 받아서 세금을 계산하는 프로그램을 작성하세요.
# wal = int(input('급여 : '))
wal = 600
income = 0;
pay = 0;
# 연소득은 급여가 500이상이면 '급여'의 12배이고,
# 500미만이면 '급여'의 13배입니다.
if wal >= 500 :
    income = wal*12
else :
    income = wal*13
# 세금은 다음 공식에 의하여 구합니다.
# 연소득(income)이
# 1구간: 0 <= income < 1000	:  0%
# 2구간: 1000 <= income < 5000	: 10%
# 3구간: 5000 <= income < 7000	: 12%
# 4구간: 7000 <= income < 10000	: 15%
# 5구간: 10000 <= income < 무한대	: 20%
# 으로 적용하면 됩니다.
if income >= 0 and income < 1000 :
    pay = 0
elif income >= 1000 and income < 5000 :
    pay = income*0.1
elif income >= 5000 and income < 7000 :
    pay = income*0.12
elif income >= 7000 and income < 10000 :
    pay = income*0.15
else:
    pay = income*0.2
form = f'''급여 : {wal}
연소득 : {income}
세금 : {pay:.0f}'''
print(form)
# 예시 01
# 급여 : 600
# 연소득 : 7200
# 세금 : 1080