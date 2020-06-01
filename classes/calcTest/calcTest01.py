result = 0
def calc(num):
    # 이변수는 함수 외부에 있는 변수입니다.
    global result # 참조가 유지된다.
    result += num
    return result


print(calc(3))
print(calc(4))

for idx in range(5,11):
    print(calc(idx))