# lambda(람다) 함수
#     return 구문 없이 함수의 역할을
#     긴 코딩량을 줄인다.

def hap(x, y):
    return x + y
x, y = 3, 5
result = hap(x, y)
print('일반 함수 방식 : %d' %( result ))

lambda1 = lambda x, y=2: x + y # lambda 매개변수 : 작업 ;
result = lambda1(x)
print('람다 방식 01 : %d' %(result))
result = lambda1(5,7)
print('람다 방식 02 : %d' %(result))

print('#list 내에 lambda 함수 사용하기')

mylist = [lambda a,b : a+b,lambda a,b : a*b]
print(mylist)
print(mylist[0](5,4))
print(mylist[1](5,4))

lambda2 = lambda a,*tu,**di : print('출력01 :',a,'\n출력02 :',tu,'\n출력03 :',di)

lambda2(1,2,3,kim=10,park=30)

print('# 다른 함수와 같이 사용해보기')
lambda3 = lambda x : x%3 != 0

# filter(함수 , 연속형 데이터)
result = list(filter(lambda3,range(10)))
print(result)

mylist =[2,5,7]
lambda4 = lambda x : [i**2 for i in x]
print(lambda4(mylist))

