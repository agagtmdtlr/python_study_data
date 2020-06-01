writelen = int(input('정수 입력 : '))
list1 = list()
sum1 = sum2 = 0
for i in range(writelen):
    write = int(input(f'{i+1}번째 점수 : '))
    if write%2!=0:
        sum1 += write
    else:
        sum2 += write
    list1.append(write)
print(f'리스트 출력 : {list1}\n홀수 총합 : {sum1}\n짝수 총합 : {sum2}')