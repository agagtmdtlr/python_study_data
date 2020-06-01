import numpy as np
import pandas as pd
import math
from pandas import DataFrame,Series

myframe = pd.read_csv('excel_pandas.csv',encoding='utf-8')
# myframe.rename(columns={'Unnamed: 0':'name'},inplace=True)
# print(myframe)

# 사람 이름을 이용하여 역순으로 정렬해보세요.
# type 컬럼은 내림차순, age 컬럼을 오름차순으로 정렬해보세요.
# print(myframe.sort_values(by=['type','age'],
#                           ascending=[True,False]))
# print(myframe.sort_values(by=['name'],ascending=[False]))

# 연령대 별 비율을 구해 보세요.(value_counts 메소드)
# 20대 또는 30대 또는 50대를 조회하세요.(isin 메소드)
# ageseries = myframe['age'].value_counts()
# total = ageseries.sum()
# print(np.round(ageseries.div(total)*100,1))

# cond = myframe['age'].isin(values=['20대','30대','50대'])
# print(cond)
# print(myframe[cond])

# 비어 있는 데이터들은 모두 30으로 대체하세요.
# 값이 가장 큰, 작은 사람은 누구인가?(idxmax 메소드)
myframe['amount'].fillna(value=30,inplace=True)
# print(myframe)
# maxs = myframe['amount'].idxmax()
# mins = myframe['amount'].idxmin()
# print(myframe.iloc[[maxs,mins]])

# 중복되지 않는 카테고리의 수는 몇개인가?
# (정답 : 컴퓨터/게임/여행/운동 총 4개)
# print(myframe['category'].unique())

# 'click' 비어 있는 데이터를 모두 1로 대체하세요.
# 총 클릭수는 얼마인가?
# 평균 클릭수는 얼마인가?
myframe['click'].fillna(value=1,inplace=True)
# print(myframe['click'].sum())
# print(myframe['click'].mean())

# 비어 있는 컬럼에 대하여 수우미양가를 판별하시오.
cond = myframe['amount2'].isnull()
# print(cond)

def grading(x):
    if x >= 90:
        return '수'
    elif x >= 80:
        return '우'
    elif x >= 70:
        return '미'
    elif x >= 60:
        return '양'
    elif x < 60:
        return '가'
# amount 칼럼의 값을 apply func arg로 넘겨서 판별후
# 적절한 값을 amount2 해당 인덱스이 값에 할당한다.

#case 1번 탐색이 2n으로 2번 증가한다. 할당변수 : n ,대입변수 : n
# myframe.loc[cond,'amount2'] = myframe.loc[cond ,'amount'].apply(grading)

#case 2번 탐색이 n번
for idx,i in myframe['amount2'].items():
    # print(idx,type(i))
    if type(i) == float:
        # print('실수')
        if math.isnan(i):
            x = myframe.loc[idx,'amount']
            myframe.loc[idx,'amount2'] = grading(x)
            # print('처리')

print(myframe['amount2'])

# 데이터 프레임에 대한 통계 정보를 조회해 보세요.(describe 메소드)
# print(myframe.describe())

