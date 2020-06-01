import numpy as np
import pandas as pd
from pandas import DataFrame,Series

myframe = pd.read_csv('excel_fillna_dropna.csv',encoding='utf-8')

# amount 값이 존재하는 회원만 조회하여 사람 이름에 대하여 내림차순으로 정렬해보세요.
# cond = myframe['amount'].notnull()
#
# view1 = myframe.loc[cond]
# print(view1.sort_values(by='amount',ascending=False))

# cond = myframe['amount'].isnull()
#
# view1 = myframe.loc[cond]
# view1.sort_values(by='name',ascending=True)

myframe.dropna(inplace=True,subset=['amount'])
# print(myframe.sort_values(by='name',ascending=True))
print(myframe['amount'])

# 각 컬럼마다 기본 값을 지정하되, 기본 값은 임의로 지정하도록 합니다.

def setDefault(x):
    # print(x.name)
    # print(type(x))
    dicts = {'name':'무명인','gender':'중성','age':'0대','job':'무직','type':'공익 광고','category':'숨쉬기','amount2':'미'}
    if not x.name in ('click','amount'):
        myframe[x.name] = x.fillna(value=dicts[x.name])

myframe.apply(setDefault)
# print(myframe)

# myseries = Series(concat_data=np.array([1,1,np.nan,1,1]),index=['a','b','c','d','e'])
# dicts = {'c':1,'d':1}
# myseries.fillna(value=dicts,inplace=True)
# print(myseries)
#
# for i in ('click','amount'):
#     cond = myframe[i].notnull()
#     avg = myframe.loc[cond,i].mean()
#     myframe.loc[~cond,i] = avg
#     print(myframe[[i]])

