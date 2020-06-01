import random


# for idx in range(10):
#     answer = random.randint(1,5)
#     print(answer)

answer = random.randint(1,100)
cnt = 1;
while True:
    my = int(input('입력 요망 : '))
    if my == answer:
        print(f'정답이군요.\n{cnt}번 만에 맞추셨군요')
        break
    elif my >= answer:
        print('더 작은수 넣어라')
    else :
        print('더 큰수 넣어라')
    cnt += 1