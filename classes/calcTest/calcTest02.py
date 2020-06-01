result1 = 0
result2 = 0

def calc1(num):
    # 이변수는 함수 외부에 있는 변수입니다.
    global result1 # 참조가 유지된다.
    result1 += num
    return result1

def calc2(num):
    global result2
    result2 += num
    return result2

print(calc1(3))
print(calc1(4))
print('-'*20)

print(calc2(5))
print(calc2(6))
print('-'*20)