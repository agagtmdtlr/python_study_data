# 몇 가지 함수들에 대한 예시
print('sum([3,4]) :',sum([3,4]))
print('sum({3,4}) :',sum({3,4}))
print('sum((3,4)) :',sum((3,4)))
print('# min,max 함수도 동일합니다.')

print('bin(8) :',bin(8)) # 2진법
print('oct(10) :',oct(10)) # 8진법
print('hex(20) :',hex(20)) # 16진법
print('int(34.56) :',int(34.56))
print('float(12) :',float(12))
print('월드컵 2002 :','월드컵 ' + str(2002)) #문자와 문자 결합 형 변환 주의
# eval : 입력받은 문자열로 함수나 클래스를 동적으로 실행할때 사용
print('eval(\'3+5\') :',eval('3+5'))
print('round(45.67) :',round(45.67))

mylist = [True,1,False]
print('all(mylist) :',all(mylist)) #전부다 참이면 true
print('any(mylist) :',any(mylist)) #하나라도 참이면 true

mylist = [1,2,3,4,5,6]
print('모든 숫자가 4보다 작습니다? :',all( idx < 4 for idx in mylist))
print('임의의 숫자가 4보다 작습니다? :',any( idx < 4 for idx in mylist))

print('aa :', ord('c')) # 문자를 아스키값으로
print('chr(65) :',chr(65))


