import pandas as pd
import numpy as np
from pandas import DataFrame,Series

cls1 = pd.read_csv('data01.csv')
cls2 = pd.read_csv('data02.csv',header=None)
# 컬럼명 수정
cls2.columns = ['이름','성별','국어','영어','과학']
cls1['class'] = '1반'
cls2['class'] = '2반'
condf = pd.concat([cls1,cls2],ignore_index=True)

# print(condf)
print('-'*50)

dicts = {'성별':['남자','여자'],
                 '국어':30,'영어':40,'수학':50,'과학':60}
for item in dicts.items():
    if item[0] == '성별':
        condf['성별'] = condf['성별'].apply(lambda i : dicts['성별'][i-1])
    else:
        try:
            condf.loc[condf[item[0]].isnull(),item[0]] = item[1]
        except Exception as err:
            print(err)


# 총점 칼럼 추가하기
condf['총점'] = condf.loc[:,['국어','영어','수학','과학']].sum(axis=1)
# 총점이 가장 높은 학생
print(condf.loc[[condf['총점'].idxmax(axis=0)],:])

idx = condf.loc[condf['class'] == '1반','총점'].idxmax(axis=0)
print(condf.loc[[idx],:])

print(condf.loc[condf['성별']=='남자','국어'].mean())
print(condf.loc[condf['성별']=='여자','수학'].sum())

check = condf.loc[:,['국어','영어','수학','과학']].mean(axis=1)
print(check)
def grading(x):
    if x >= 40 :
        return '합격'
    else:
        return '불합격'

condf['합격여부'] = check.apply(grading)
print(condf)


condf['등수'] = condf['총점'].rank(ascending=False)
print(condf)