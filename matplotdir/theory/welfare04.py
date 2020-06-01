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
# 연령대별/성별
thisyear = 2020
myframe['age'] = thisyear - myframe['birth'] + 1

def newAge(x):
    if x < 30:
        return '청년'
    elif x >= 30 and x < 60:
        return '중년'
    else :
        return '노년'

myframe['ageg'] = myframe['age'].apply(newAge)

#성별
myframe.loc[myframe['gender']==1,['gender']] = '남자'
myframe.loc[myframe['gender']==2,['gender']] = '여자'

print(myframe[['gender','age','ageg']].head(10))

ageg_income = myframe.dropna(subset=['income'])
mygrouping = ageg_income.groupby(by=['ageg','gender'])['income']
mydata = mygrouping.mean().unstack(1) # level= 0,1 해당 레벨 인덱스를 컬럼으로
print(mydata)
print(type(mydata))
mydata.columns.name = '성별'
mydata.index.name = '연령대'

mydata.plot(kind='bar',rot=0, alpha=0.7, stacked=True)
plt.legend()


filename = 'data/welfare_04_01.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')
