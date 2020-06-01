import math
jumlists = []
partnum = dict()
titlelist = []
with open(file='data/memdata02.csv',mode='r',encoding='utf-8') as file :
    w = [80,10,10]
    m = [1000,100,100]
    part = ['','기술지원부','영업부','총무부','인사부'] #주어진 부서별 코드숫자에 맞게 리스트를 만든다.
    level = ['','사원','주임','대리','팀장'] #주어진 직급별 코드숫자에 맞게 리스트를 만든다.
    while True: # 각 행 데이터를 뽑아와 3개의 파트 작업을 수행할 것이다.
        line = file.readline()
        if not line:
            break
        line = line.replace('\n','').split(',') # 개행문자'\' 없애고, 데이터 쪼개기까지

        #dict에 부서별 인원체크
        pi = int(line[1]) # 데이터 코드를 인덱싱에 활용하기 위해 정수형 타입으로 변환
        if part[pi] in partnum: #해당 코드로 part list에 인덱싱하여 해당 키값 부서명이 dict에 존재하는지 판별한다.
            partnum[part[pi]] = partnum[part[pi]]+1 #이미 키가 존재한다면 기존값에 더하기
        else:
            partnum[part[pi]] = 1 #키가 없다면 1로 초기화하여 선언하기

        #직원별 점수
        jum = [int(i) for i in line[3:6]]
        result = round(sum([ jum[i]/m[i]*w[i] for i in range(len(jum))]),2)
        jumlists.append([line[0],str(result)])

        #이름 부서 직위 표시
        # 데이터 숫자형 변환 후 -> 각 theme에 맞는 리스트를 통해 인덱싱하여 문자자료로 변화후 결과물 변수에 저장하기
        titlelist.append([line[0],part[int(line[1])],level[int(line[2])]])

print(partnum)
print(jumlists)
print(titlelist)

with open(file='data/result02.txt',mode='w',encoding='utf-8') as file :
    for i in titlelist:
        file.write('/'.join(i)+'\n')