import numpy as np
import pandas as pd
from pandas import DataFrame

dict1 = {'name':['홍길동','홍길동','김철수','박영희','김철수','김철수','홍길동'],'korean':range(7)}
df1 = DataFrame(dict1)

dict2 = {'name':['김철수','홍길동','심수봉'],'english':range(3)}
df2 = DataFrame(dict2)

print(df1)
print('-'*20)

print(df2)
print('-'*20)

print(pd.merge(df1,df2,on='name', how='inner')) # 키 컬럼 공동된것을 결합
print(pd.merge(df1,df2,on='name', how='outer')) # 키 컬럼 모든것을 결합
print(pd.merge(df1,df2,on='name', how='left')) # 키 컬럼 왼족df모든것을 결함
print(pd.merge(df1,df2,on='name', how='right'))
print('-'*20)
#
dict3 = {'leftkey':['홍길동','홍길동','김철수','박영희','김철수','김철수','홍길동'],'korean':range(7)}
df3 = DataFrame(dict3)

dict4 = {'rightkey':['김철수','홍길동','심수봉'],'english':range(3)}
df4 = DataFrame(dict4)

print(pd.merge(df3,df4,left_on='leftkey',right_on='rightkey'))
print('-'*20)

dict5 = {'key1':['김철수','김철수','박영희'], 'key2':['one','two','one'], 'leftval':[1,2,3]}
df5 = DataFrame(dict5)
print(df5)
print('-'*20)

dict6 = {'key1':['김철수','김철수','박영희','박영희'], 'key2':['one','one','two','one'], 'leftval':[4,5,6,7]}
df6 = DataFrame(dict6)
print(df6)
print('-'*20)

# 여러개의 키를 사용해 조인
mylist = ['key1','key2']
print(pd.merge(df5,df6,on=mylist,how='outer'))
print('-'*20)
# suffixes 중복되는 컬럼명 구별시켜주기
print(pd.merge(df5,df6,on=mylist,how='outer',suffixes=('_왼쪽','_오른쪽')))
print('-'*20)

# 해당 칼럼 으로 색인 만들기
newdf1 = df1.set_index('name')
newdf2 = df2.set_index('name')

print(newdf1)
print(newdf2)

# 색인을 통한 merge
print(pd.merge(newdf1,newdf2,left_index=True,right_index=True))
print(pd.merge(newdf1,df2,left_index=True,right_on='name'))
print(pd.merge(df1,newdf2,left_on='name',right_index=True))
print(pd.merge(df1,df2,on='name',how='outer',indicator=True))