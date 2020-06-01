name = '김철수'
fruit = '사과'
su1 = 8

myformat = '%s이(가) %s를 %d개 먹었습니다.'
print(myformat %(name,fruit,su1))

su1 = 4
su2 = 9
result = su1 * su2
myformat = '%d 곱하기 %d 는 %d입니다.'
print(myformat %(su1,su2,result))

a = 2.7
b = 3.5
#pow(a,b)는 a의 b제곱을 해주는 내장 함수 입니다.

result = pow(a,b)
result = pow(int(a),int(b))
myformat = "%.f의 %.f승은 %.f입니다."
print(myformat %(a,b,result))

print('%를 표현하려면 %%를 표시해야 합니다.')
rate = 0.4567
print('비율 : %.2f%%' %(100*rate))

a,b = 14,5

sum = a + b
sub = a - b
multiply = a * b
divide = a / b
remainder = a % b # 나머지
power = 2 ** 10 # 1024

print('덧셈 : %d' %sum)
print('뺄셈 : %d' %sub)
print('곱하기 : %d' %multiply)
print('나누기 : %d' %divide)
print('나머지 : %d' %remainder)
print('제곱수 : %d' %power)

su = 12.3456789
print('나눗셈 : [%f]' %(su))
print('나눗셈 : [%.2f]' %(su))
print('나눗셈 : [%6.2f]' %(su))
print('나눗셈 : [%-6.2f]' %(su))

#input 함수를 사사용하여 다음과 같이 출력되게 프로그램밍
# 홍길동님의 점수 현황
# 국어 : 60 , 영어 : 71
# 총점 ; 131, 평균 : 65.500입니다.

kor,eng = int(input('국어 : ')),int(input('영어 : '))

total = kor + eng
avg = total/2
result="""홍길동님의 점수 현황
        국어 : %d , 영어 : %d
        총점 : %d , 평균 : %6.3f입니다"""
print(result %(kor,eng,total,avg))