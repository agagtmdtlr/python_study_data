import pandas as pd
import random

result = []
mycolumns = ('번호','이름','나이')

for idx in range(1, 3):
    sublist = []
    sublist.append(100 * idx)
    sublist.append('김철수'+str(idx))
    sublist.append(random.randint(1,10))
    result.append(sublist)

myframe = pd.DataFrame(result, columns=mycolumns)

filename = 'result01.csv'

myframe.to_csv(filename,encoding='utf-8', mode='w', index=True)

print(filename + '파일 저장 완료')