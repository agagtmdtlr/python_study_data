import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

filename = 'data/welfare_python.csv'
myframe = pd.read_csv(filename,encoding='utf-8')



# for idx,val in myframe['age'].items():
#     if val <10 or val >= 60:
#         myframe.drop(idx,inplace=True)

myframe['age'] = 2020 - myframe['birth'] +1
# cond1 = myframe['age']>10
# cond2 = myframe['age']<=60
# condf = myframe[cond1 & cond2]

# myframe[myframe['age']<10] = np.nan
# myframe[myframe['age']>=60] = np.nan
# myframe.dropna(subset=['age'],inplace=True)

myframe.mask(lambda x : x['age']<10,inplace=True)
myframe.mask(lambda x : x['age']>=60,inplace=True)
myframe.info()