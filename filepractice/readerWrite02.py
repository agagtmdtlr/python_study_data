dicts = dict() # 파일 행마다 데이터를 가공해 저장할 dict를 준비한다.
with open(file='data/jumsu.txt',mode='r',encoding='utf-8') as file:
    while True:
        line = file.readline() # 한 줄씩 읽는다.
        if not line:
            # 만약 줄이 끝났다면
            # 더 이상 불러올 데이터가 없으므로 none이다.
            # 반복문을 빠져나간다.
            break
        # 행끝 있는 개행문자'\n'을 지우고
        # 데이터가 ','로 구분되어 있으므로 split()으로 쪼갠다.
        # 쪼개진 데이터는 list로 반환된다.
        # 주의할점 읽어온 모든 파일 데이터는 str타입이다
        line = line.strip().split(',')
        # list 끝에 데이터는 code 성별을 판별
        if line[-1].upper() == 'F':
            gender = '여자'
        else :
            gender = '남자'
        # 이름 성별을 제외한 중간에 있는 점수를 float타입을 변환후 sum()을 산술
        total = sum([float(x) for x in line[1:4]])
        # 평균 후 round()로 소수점 2번째 자리까지 반올림하여 정리
        avg = round(total/3,2)
        # 키값 이름 : 성별,총합,평균
        dicts[line[0]] = [gender,total,avg]
    # 반복문이 끝나면 dict를 출력하여 결과 학인한다.
    print(dicts)

# 가공한 데이터를 파일에 저장하기
with open(file='data/result.txt',mode='w',encoding='utf-8') as file:
    for k,v in dicts.items():
        v[2] = str(v[2]).ljust(5,'0')
        data = k+'/'+'/'.join(map(str,v))+'\n'
        file.write(data)