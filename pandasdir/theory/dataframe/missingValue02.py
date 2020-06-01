import numpy as np
import pandas as pd
from pandas import DataFrame,Series

myframe = pd.read_csv('excel02.csv', index_col='이름',encoding='utf-8')
# index_col : csv 파일에 해당 칼럼을 인덱스로 사용하겠다.
# print(myframe)
# print('-'*20)

# print(myframe.dropna(axis=0,how='all'))
# print(myframe.dropna(axis=0,subset=['영어']))

myframe.loc[['강감찬','홍길동'],['국어']] = np.nan
print(myframe)

print(myframe.dropna(axis=1,how='all'))
print('-'*40)

print(myframe.dropna(axis=1,how='any'))
print('-'*40)

print(myframe.dropna(axis=1,thresh=2)) # thresh Require that many non-NA values
print('-'*40)
