# ageInfo.pyy
# 이름과 나이를 입력 받으세요.
# 다음과 같이 출력하는 프로그램을 만들어 보세요.
# 40세 이상이면 '중년',
# 30세 이상이면 '청년',
# 19세 이상이면 '성년',
# 미만이면 '미성년'으로 출력해주는 프로그램을 작성하세요.
name,age = input('이름,나이 : ').split(',')
age = int(age)
check1 = ''
if age>=40:
    check1='중년'
elif age>=30:
    check1='청년'
elif age>=19:
    check1='성년'
else:
    check1='미성년'
print(f'나이 : {age} 연령대 : {check1}')