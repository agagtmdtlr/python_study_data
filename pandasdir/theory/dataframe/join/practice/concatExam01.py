import pandas as pd
import numpy as np
from pandas import DataFrame

df1 = pd.read_csv('sample01.csv',encoding='utf-8')
df2 = pd.read_csv('sample02.csv',encoding='utf-8')

df1['remark'] = '중간'
df2['remark'] = '기말'

condf = pd.concat([df1,df2],join='outer',ignore_index=True)
print(condf)
for i in ['국어','영어','수학']:
    condf.loc[condf['국어'].isnull(),'국어'] = condf['국어'].mean(axis=0,skipna=True)
print(condf)


df1.set_index('이름',inplace=True)
df2.set_index('이름',inplace=True)

mdf = pd.merge(df1.loc[:,['국어','영어','수학']],
               df2.loc[:,['국어','영어','수학']],
               left_index=True,right_index=True,
               suffixes=('중간_','기말_'))
print(mdf)

# condf2 = pd.concat([df1,df2],axis=1)
# print(condf2)