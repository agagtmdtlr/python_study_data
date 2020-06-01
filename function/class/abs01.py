def absolute(su):
    if su < 0:
        #su = -1*su
        su = ~su +1 #비트연산
        su = -su #부호 연산자
    return su

num = -5
num = absolute(num)
print(num)

list1 = [2,-4,7]
list1 = [absolute(i) for i in list1]
print(list1)