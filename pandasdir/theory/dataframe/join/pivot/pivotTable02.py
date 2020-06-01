import numpy as np
import pandas as pd
from pandas import Series

filename = 'fruit_sales.csv'
fruits = pd.read_csv(filename, encoding='utf-8')
print(fruits)
print('-'*50)

fruits_melt = pd.melt(fruits,id_vars=['city','year','month'],var_name='item',value_name='qty')
print(fruits_melt)
print('_'*50)

fruits_pivot = fruits_melt.pivot_table(index=['city','year'],
                                       columns=['month','item'],
                                       values='qty',
                                       aggfunc=np.sum)
print(fruits_pivot)
print('_'*50)
fruits_tidy = fruits_melt.pivot_table(index=['city','year'],
                                       columns='month',
                                       values=['item','qty'],
                                       aggfunc={'item':'count','qty':np.mean})
print(fruits_tidy)
print('_'*50)
# 품목(item)별 합계(sum) 구하기
fruits_pivot = fruits_melt.pivot_table(index=['city','year'],
                                       columns='item',
                                       values='qty',
                                       aggfunc={'qty':'sum'})
print(fruits_pivot)
print('_'*50)

fruits_pivot = fruits.pivot_table(index=['city','year'],
                                  columns='month',
                                  values=['사과','배','감','대추','복숭아'])
print(fruits_pivot)

from pandas import Series
def hab(x):
    if isinstance(x,Series):
        print('Series')
    return 0

fruits_pivot = fruits_melt.pivot_table(index=['city','year'],
                                       columns='item',
                                       values='qty',
                                       aggfunc={'qty':hab})
print(fruits_pivot)
