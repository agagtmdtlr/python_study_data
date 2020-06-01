import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

filename = 'data/welfare_python.csv'
myframe = pd.read_csv(filename,encoding='utf-8')
myframe.info()
print('-'*30)

# 생일
print(sum(myframe['birth'].isnull())) # 결측치
print('-'*30)

myframe['birth'].plot(kind='hist', bins=50,alpha=0.7,title='생일별 빈도',xlim=[1900,2020])

filename = 'data/welfare_02_01.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')

# 나이(age) : 파생 칼럼 만들기
thisyear = 2020
myframe['age'] = thisyear - myframe['birth'] + 1
print(myframe['age'].describe()) # 연속형 데이터 이상치 확인하기

myframe['age'].plot(kind='hist', bins=50,alpha=0.7,title='나이별 히스토그램')

filename = 'data/welfare_02_02.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')

# 나이 그룹핑 / 나이별 소득 평균
age_income = myframe[pd.notnull(myframe['income'])]
mygrouping = age_income.groupby(by='age')['income']
mydata = mygrouping.mean()
print(mydata)

mydata.plot(kind='line', rot=0,marker='o')

plt.xlabel('나이')
plt.ylabel('평균 소득')
plt.title('나이별 평균 소득')
plt.xticks([idx for idx in range(20,101,10)])

filename = 'data/welfare_02_03.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')

# 범주화
def newAge(x):
    if x < 30:
        return '청년'
    elif x >= 30 and x < 60:
        return '중년'
    else:
        return '노년'
myframe['ageg'] = myframe['age'].apply(newAge)
print(myframe['ageg'].head())
print(myframe['ageg'].unique())

mygrouping = myframe.groupby(by='ageg')['ageg']
mydata = mygrouping.count()

mydata.plot(kind='bar', rot=0)

plt.xlabel('연령대')
plt.ylabel('빈도수')
plt.title('연령대별 빈도수')

filename = 'data/welfare_02_04.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')

# 소득이 있는 사람중에서 연령대별로 평균 값 구하기

mygrouping = myframe[myframe['income'].notnull()].groupby(by='ageg')['income']
mydata = mygrouping.mean()

ax = mydata.plot(kind='bar', rot=0, color=['r','g','b'])
plt.xlabel('연령대')
plt.ylabel('평균 소둑')
plt.title('연령대별 평균 소득')

filename = 'data/welfare_02_05.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')

# plt.show()
print('finished')