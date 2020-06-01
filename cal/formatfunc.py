su = 3
fruit = '사과'

# {}는 치환이 될 영역을 의미합니다.
str1 = '나는 {}를(을) {}개 먹었습니다.'
print( str1.format(fruit,su))
print('-'*30)
str1 = '나는 {0}를(을) {1}개 먹었습니다.'
print( str1.format(fruit,su))
print('-'*30)
str1 = '나는 {1}를(을) {0}개 먹었습니다.'
print( str1.format(su,fruit))
print('-'*30)
print('keywoard argument')
# {abc}와 {defg} 는 keyword name이라고 합니다.
str4 = '나는 {abc}를(을) {defg}개 먹었습니다'
print(str4.format(defg=su, abc=fruit))
# indect number 와 keyword name을 혼합한 방식
print('2가지 방식 혼합')
str5 = '나는 {abc}를(을) {}개 먹었습니다.'
print(str5.format(su,abc=fruit))
str5 = '나는 {abc}를(을) {}개 먹었습니다.'
# print(str5.format(abc=fruit,su)) :
# SyntaxError: positional argument
# follows keyword argument
str5 = '나는{0} {abc}를(을) {1}개 먹었습니다.'
print(str5.format(12,su,abc=fruit))
# 중괄호 {}는 format() 함수에 사용되는 치환될 대상이다.

print('고급 formatting 기법')
hello = 'hello!'

print('왼쪽 정렬 : [{0:<10}]'.format(hello))
print('-'*30)
print('오른쪽 정렬 : [{0:>10}]'.format(hello))
print('-'*30)
print('가운데 정렬 : [{0:^10}]'.format(hello))
print('-'*30)

print('왼쪽 정렬에 패딩 : [{0:*<10}]'.format(hello))
print('-'*30)
print('오른쪽 정렬에 패딩 : [{0:*>10}]'.format(hello))
print('-'*30)
print('가운데 정렬에 패딩 : [{0:*^10}]'.format(hello))
print('-'*30)

name1 ='허각'
name2 = '홍길동'
name3 = '선우재덕'

format1 = '{0:5}{1}[{2:>5}]'
print(format1.format(name1,'   ',12))
print(format1.format(name2,'  ',123))
print(format1.format(name3,' ',1234))

# 소수점 표현하기 ,format()안에서 {}문자로 표현
y = 3.42134234
format1 = '{0:5.4f} , {{and}}'
print(format1.format(y))

# f 포맷팅
name1 ='허각'
age = 30
format1 = f'나의 이름은 {name1}입니다. 나이는 {age}입니다'
print(format1)