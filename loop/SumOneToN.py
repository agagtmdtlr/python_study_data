#임의 정수(변수n)를 1개 입력 바다아서 , 1부터 n까지의 총합 구하기
#단 음수가 나오면 절대값으로 변경하여 풀어 봅니다.
n = abs(int(input('정수 : ')))
total = 0
for i in range(1,n+1):
    total += i
print('1부터 %d까지 총합은 %d입니다' %(n,total))