# numeric_type.pyy
# 숫자는 따옴표를 붙이지 않습니다.
from builtins import print

a = 123
print(a)
print('-' * 20)
a = -178
print(a)
print('-' * 20)
a = 4.24E3 # *1000
print(a)
print('-' * 20)
a = 1234E-2 # /100
print(a)
print('-' * 20)
a = 0o10 # 8진수는 앞에 '영과 알파벳o'을 붙여준다
print(a)
print('-' * 20)
a = 0x10 # 16진수는 앞에 '영과 알파벳x'을 붙여준다
print(a)
print('-' * 20)
print('연산자')
a = 3
b = 4
print('덧셈 :', (a+b)) # +
print('뺄셈 :', (a-b)) # -
print('곱셈 :', (a*b)) # *
print('나눗셈 :', (a/b)) # /
print('몫 :', (a//b)) # //
print('몫2 :', (17//5)) # //
print('나머지 :', (17%5)) # /

# divmod : 몫과 나머지를 튜플 형태로 출력해주는 함수입니다. divmod(분자,분모)
print(divmod(17,5))