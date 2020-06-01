# print01.pyy

# print('이름 입력 해주세요')
# name = input()
#
# age = input('나이 입력해주세요.')
#
# print('제 이름은',name,'나이는',age)

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# *은 가변 매개 변수를 의미합니다. 매개변수의 개수가 가변적인다.
# print('동해물과','백두산이','마르고','닳도록') # 문자별로 띄워 쓰기
# print('동해물과' '백두산이' '마르고' '닳도록') # 문자열 결합
#
# # sep=''는 구분자이다.
# print('동해물과','백두산이','마르고','닳도록',sep=' ')
# print('동해물과','백두산이','마르고','닳도록',sep='호호')
#
# # end=''는 출력 마지막 행의 값을 지정한다. 띄어쓰기?다음 줄.
# print('안녕하세요',end=' ')
# print('홍길동님',end='\n')

# file : 출력 위치를 지정하는 옵션입니다.

# stdout : Standard Output Device --> sys.stdout 모니터

# input()의 반환값은 문자열 입니다.
# name = input('이름 입력 해주세요')
#
# age = input('나이 입력해주세요.') #나이가 문자로 받아짐
#
# print('제 이름은',name,'나이는',age)
#
# newage = int(age) + 5 #숫자형 변환 후 연산 해야됨
# print('5년뒤 나이',newage)

#국영수 점수 3개를 입력 받아서,총합을 구해보세요
kor,eng,math =  input('국어 영어 수학').split(',')
kor = int(kor)
eng = int(eng)
math = int(math)
total = kor+eng+math
print(kor+eng+math)

#placeholder : {} 0번째 인덱스 부터 시작합니다.
print('{}+{}+{}={}'.format(kor,eng,math,total))