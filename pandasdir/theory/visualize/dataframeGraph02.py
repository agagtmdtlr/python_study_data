import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')

filename = 'data/ex802.csv'
myframe = pd.read_csv(filename,index_col='type',encoding='utf-8')
myframe.index.name = '자동차 유형'
myframe.columns.name = '도시(city)'
myframe = myframe.T # 유형별 지역 등록대수
print(myframe)
print('-'*30)

myframe.plot(kind='bar',rot=0,title='유형별 지역 등록대수',legend=True, stacked=True)
# myframe.plot(kind='bar',rot=0,title='지역별 차량 등록대수',legend=True)
#
filename = 'data/bargraph03.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+'파일 저장 완료')

plt.show()