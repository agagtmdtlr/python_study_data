import numpy as np
import pandas as pd
from pandas import DataFrame

filename = 'left1.csv'

# 첫번째 열을 인덱스로 처리하여 가져온다.
left1 = pd.read_csv(filename,encoding='utf-8',index_col=0)
print(left1)
print('-'*20)

filename = 'right1.csv'

right1 = pd.read_csv(filename,encoding='utf-8',index_col=0)
print(right1)
print('-'*20)


print(pd.merge(left1,right1,left_on='name',right_index=True))