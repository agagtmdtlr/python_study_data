num = int(input('정수 입력 : '))
if num < 0 : num = abs(num)
for i in range(1,10):
    print(f'{num}*{i}={num*i:2d}',end=' ')
print()
cnt = 0
while True:
    print('a')
    cnt += 1
    if(cnt == 5):
        break