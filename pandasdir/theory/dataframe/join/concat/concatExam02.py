import pandas as pd
from pandas import DataFrame

df1 = pd.read_csv('concat_1.csv')
df2 = pd.read_csv('concat_2.csv')
df3 = pd.read_csv('concat_3.csv')

# axis = 0/1 : index/column
# ignore_index = bool : 기존 인덱스 무시 여부
concatRow = pd.concat([df1,df2,df3], axis=0,ignore_index=True)
print(concatRow)

newframe = DataFrame([[11,22,33,44]],
                     columns=['서울','부산','대구','인천'])
print('pd.concat/ df.append 함수')
print(pd.concat([df1,newframe],axis=0))
print(df1.append(newframe))

concatRow = pd.concat([df1,df2,df3], axis=1)
print(concatRow)
print('-'*40)

print(concatRow['서울'])
print('finished!')

df1.columns = ['서울','부산','대구','인천']
df2.columns = ['서울','부산','경주','포항']
df3.columns = ['서울','부산','대전','울산']

result = pd.concat([df1,df2,df3], axis=0)
print(result)

result = pd.concat([df1,df2,df3], join='inner', axis=0)
print(result)

df1.index = [0,1,2,3]
df2.index = [4,5,6,7]
df3.index = [0,2,5,7]

# 인덱스도 중복여부를 체크하여 포함시키거나 추가한다.
result = pd.concat([df1,df2,df3], axis=1)
print(result)

result = pd.concat([df1,df3],axis=1,join='inner')
print(result)