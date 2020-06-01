str1 = '100'
str2 = '200'
str3 = '12.345'

int1 = int(str1)
int2 = int(str2)
float1 = float(str3)

print(type(int1) == str)
print(int1 == str) # type()함수를 안써도 자동을 타입 비교를 해주네

sum = int1 + int2
print('출력1: ',sum)

float2 = float1 + 35.2
print('출력2:',float2)

print(type(str1))
print(type(int1))
print(type(float1))