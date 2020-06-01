a=10
b=20
print('관계연산자')
result = a >= b
print(result)
print('-'*30)

result = a < b
print(result)
print('-'*30)

result = a == b
print(result)
print('-'*30)

result = a != b
print(result)
print('-'*30)

print('논리연산자')
first = a >= b # 10 >= 20 이므로 false
second = a != b # 10 != 20 이므로 true

result = first and second # false and true 이므로 false
print(result)
print('-'*30)

third = a == b # 10 == 20 이므로 false
result = (first and second) or third
# false and true or false 이므로 false
print(result)
print('-'*30)

result = not(result) # false가 아니다 이므로 true

x = 1

x += 4
print('x:',x)
print('-'*20)

x *= 5
print('x:',x)
print('-'*20)

x %= 6
print('x:',x)
print('-'*20)

x -= 1
print('x:',x)
print('-'*20)

x += 1
print('x:',x)
print('-'*20)

total = 0
total+=1;total+=2;total+=3;total+=4;total+=5;total+=6;total+=7;total+=8;total+=9;total+=10;
total = (1+10)*(10/2)
print('total:',total)
print('-'*20)

print(int(True))

a = 10
b = 8
bool1 = a != b

a -= 1
b += 1
bool2 = a != b

a,b = 10,8
bool3 = bool2 and (5 > 7)

bool4 = not(bool3) or (bool1 and bool2)

print(bool1)
print(bool2)
print(bool3)
print(bool4)

mylist = [True,False,True,False]
# sum 함수는 합을 구해주는 내장 함수 입니다.
result = sum(mylist)
print(result)