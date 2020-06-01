
# 합격여무 판단
examdata = [90,30,65,70,89]
print('원소 1개씩 출력')
for item in examdata:
    print(item)
print('range 사용하기')
for idx in range(len(examdata)):
    print(examdata[idx])
print('합격자만 출력하보기')
for idx in range(len(examdata)):
    if examdata[idx]>=60:print('{}번째 응시자 {}점 합격'.format(idx+1,examdata[idx]))
    else : print('{}번째 응시자 {}점 불합격'.format(idx+1,examdata[idx]))
print('합격자만 출력하보기')
for idx in range(len(examdata)):
    if examdata[idx]>=60:print('{}번째 응시자 {}점 합격'.format(idx+1,examdata[idx]))
    else : continue