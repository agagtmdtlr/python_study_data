# 풀어보세요(미성년자 체크하기)
# input() 함수를 이용하여 이름과 주민 등록 번호를 입력 받으시고,
# 다음과 같이 출력하는 프로그램을 만들어 보세요.
# 나이는 금년과 주민 등록 번호
# 앞2자리를 산술 연산하여 구하면 됩니다.
# 성인은 19세 이상이라고 가정합니다.

name = input('이름 : ')
pw = input('주민번호 : ')
age = 20-int(pw[0]+pw[1])
gender = ""
check = ""
if int(pw[7]) == 1 or int(pw[7]) == 3:
    gender ='남'
else:
    gender='여'
if age >= 19 :
    check='성인'
else :
    check='미성년자'
print(f'이름 : {name}\n'
      f'주민번호 : {pw}\n'
      f'성별 : {gender}\n'
      f'나이 : {age}세\n'
      f'체크 : {check}\n')