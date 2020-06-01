# input() 함수를 이용하여 'Korea'를 입력 받으세요.
# 이 문자열의 2 번째 문자를 추출하여
# 다음과 같이 출력되는 프로그램을 작성하세요.
# 추출된 문자가 대문자/소문자/숫자/기타 문자인지
# 판별하는 프로그램을 작성하세요.
# 관계 연산자와 and 키워드를 이용하여 판별해 보세요.

mystr = input('입력 : ')
sub1 = mystr[2]
check1=''
form = f'''문자열 : {mystr}
문자 : {sub1}
대문자인가요 : {sub1.isupper()}
소문자인가요 : {sub1.islower()}
숫자인가요 : {sub1.isnumeric()}
아스키 코드 : {ord(sub1)}'''

print(form)