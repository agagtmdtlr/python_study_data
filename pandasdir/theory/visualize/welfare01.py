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