f = open(file='jumsu.txt',mode='r',encoding='utf-8')

data = f.read().strip().split(',')
total = sum([float(i) for i in data[1:4]])
avg = total/3
if data[-1] == 'F': gender = '여자'
else: gender = '남자'
f.close()

print(f'이름 : {data[0]}\n'
      f'총점 : {total}\n'
      f'평균 : {avg:.2f}\n'
      f'성별 : {gender}')
print('작업 종료')