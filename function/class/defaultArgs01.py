def fun01(a,b):
    return 2*a+b

print(fun01(3,5))
# TypeError: fun01() missing 2 required positional arguments: 'a' and 'b'
# print(fun01()) 필수사항 매개변수를 빠뜨렸다.

def fun02(a=2,b=1):
    return  2*a+b

def fun03(a=1,b=2,c=3):
    return a+b+c
print(fun02(),fun02(3),fun02(3,5))
# positional arguments : 숫자 기반으로 매개 변수를 맞춰 주는 기능 [1번째가 1번재로 2번째 2번째로 ....]

# keyword argument : 매개 변수의 이름으로 매칭하는 기능
print(fun02(b=2,a=1))
print(fun02(2,b=1))
# Positional argument after keyword argument
# SyntaxError: positional argument follows keyword argument : 포지션이 키워드보다 먼저 나와야 된다.
# print(fun02(b=1,2))

def showStar(n=5,r=10):
    for i in range(1,r+1):
        print('*',end='')
        if i%n == 0:
            print()
    print()
showStar()
showStar(3)
showStar(5,12)