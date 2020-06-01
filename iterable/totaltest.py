#
#
# 문제 01
# 다음을 list로 만들어 보세요.
# sum() 함수를 이용하여 총합을 구해 보세요.
# 정렬과 인덱싱 및 슬라이싱을 이용하여 최대와 최소 값을 구해 보세요.
# 최대와 최소를 제외한 값들의 평균을 구하세요.
# 데이터 : 80, 50, 40, 30, 90
mylist = [80,50,40,30,90]
total = sum(mylist)
mylist.sort()
mylen = len(mylist)
min = mylist[0]
max = mylist[mylen-1]
avg = sum(mylist[1:mylen-1])/(mylen-2)
form = f'''{mylist}
total : {total}
min : {min}
max : {max}
avg : {avg:.0f}'''
print(form)
# 문제 02
# 아이디    이름    나이  거주지
# hong	홍길동	23	경기
# hwang	황진이	25	서울
#
# 위의 데이터를 사전으로 만들어 보세요.
# '아이디' 컬럼은 key로 나머지 3컬럼은 list 형태로 만들어서 value으로 넣어 주면 됩니다.
mydict = dict()
mydict['hong'] = ['홍길동',23,'경기']
mydict['hwang'] = ['황진이',25,'서울']
# 다음과 같이 출력해 보세요.
# 아이디 : hong
# 이름 : 홍길동
# 나이 : 23
# 거주지 : 경기
# ---------------------
# 아이디 : hwang
# 이름 : 황진이
# 나이 : 25
# 거주지 : 서울
# ---------------------
for ky,val in mydict.items() :
    print(f'아이디 : {ky}\n'
          f'이름 : {val[0]}\n'
          f'나이 : {val[1]}\n'
          f'거주지 : {val[2]}\n'
          ,'-'*20,sep='')


