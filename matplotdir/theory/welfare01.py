import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

filename = 'data/welfare_python.csv'
myframe = pd.read_csv(filename,encoding='utf-8')
print(myframe.info())
print('-'*20)

print(type(myframe['gender']))
print('-'*20)

print(myframe['gender'].unique())
print('-'*20) # [2 1]

# 성별 : (이산형 변수) 분류형 데이터
# 월급 : (연속형 변수)

# 코딩 변경 (re_coding)
# 1 -> 남자, 2-> 여자
# 1 -> 사원, 2-> 대리 ...
myframe.loc[myframe['gender']==1,['gender']] = 'male'
myframe.loc[myframe['gender']==2,['gender']] = 'female'
print(myframe.head())
print('-'*20)

mygrouping = myframe.groupby(by='gender')['gender']
# <pandas.core.groupby.generic.SeriesGroupBy object>
mydata = mygrouping.count()
print(mydata)
print(type(mydata))

mydata.plot(kind='bar',rot=0,ylim=[0,10000],color=['r','b'] )

plt.xlabel('성별')
plt.ylabel('빈도수')
plt.title('성별에 따른 빈도')

filename = 'data/welfare_01_01.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
print(filename + '파일 저장 완료')

plt.figure()

# 연속형 데이터 확인하기
print(myframe['income'].describe())

# 결측치 개수
print(sum(myframe['income'].isnull()))

myframe['income'].plot(kind='hist',bins=150)

filename = 'data/welfare_01_02.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
print(filename + '파일 저장 완료')

plt.figure()

myframe['income'].plot(kind='hist',bins=150, xlim=(0,1000))

filename = 'data/welfare_01_03.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')

# 소득이 있는 항목 중에서 성별로 그룹핑하여 평균 급여 구해 보기.
gender_income = myframe[pd.notnull(myframe['income'])] # 소득이 있는거 추리기
print(gender_income.info())

mygrouping = gender_income.groupby(by='gender')['income'] # 성별로 그룹핑
mydata = mygrouping.mean() # 그룹 평균 계산하기
print(mydata) # result : Series

mydata.plot(kind='bar',rot=0,color=['r','b']) # bar 이산 그래프

plt.xlabel('성별')
plt.ylabel('평균 소득')
plt.title('성별에 따른 월급의 평균')

filename = 'data/welfare_01_04.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')

