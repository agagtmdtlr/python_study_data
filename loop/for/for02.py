
# 1부터 10까지 홀수의합 25,짝수의 합 30입니다
sum1 = 0 #홀
sum2 = 0 #짝
for i in range(1,11):
    if i%2 is not 0 :
        sum1 += i
    else :
        sum2 += i
print('1부터 10까지 홀수의합 %d,짝수의 합 %d입니다' %(sum1,sum2))
