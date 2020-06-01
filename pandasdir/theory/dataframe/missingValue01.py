import numpy as np
from pandas import DataFrame,Series

import os

paths = 'D:\pss\python\project1\pyy\data'
print(os.getcwd())
os.chdir(paths)
print(os.getcwd())

myseries = Series(['강감찬','이순신',np.nan,'광해군'])
print(myseries)
print('-'*20)

print(myseries.isnull())
print(myseries.notnull())

print(myseries[myseries.notnull()])
print(myseries.loc[myseries.notnull()])

print(myseries.dropna())
with open(file='excel02.csv',mode='r',encoding='utf-8') as file :
    pass