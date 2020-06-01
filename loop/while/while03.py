cnt = total = avg = 0
while True :
    no = int(input('점수입력 : '))
    if(no < 0 ):
        break
    total += no
    cnt += 1
avg = total/cnt
print(f'총시험회수 : {cnt}\n총점 : {total}\n평균 : {avg}')