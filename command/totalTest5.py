# 중간 고사는 40%, 기말 고사는 60%의 가중치를 부여합니다
# # 평균이 70점 이상이면 합격,
# 그렇지 않으면 불합격을 출력해주는 프로그램을 작성해 보세요.
# # successFail.pyy

mim,end = map(int,input('중간,기말 : ').split(','))
me = 0.4
ee = 0.6
avg = (mim*me+end*ee)/1
check = ''
if avg >= 70 :
    check='합격'
else :
    check='불합격'
print(f'중간 : {mim}\n'
      f'기말 : {end}\n'
      f'평균 : {avg:.0f}\n'
      f'체크 : {check}')