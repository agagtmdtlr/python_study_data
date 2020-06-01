import pandas as pd
import sys
import os

print(os.getcwd())
#D:\pss\python\project1\pyy\pandasdir\theory\dataframe
filename = 'D:\pss\python\project1\pyy\data\memberInfo.csv'
df = pd.read_csv(filename, index_col='id')
print(df)
print('-'*20)

# print(df['kor']+5)
# print('-'*30)
#
# def plus5(x):
#     return x + 5
#
# sq = df['kor'].apply(plus5)
# print(sq)
# print('-'*30)
#
# def gob(x,n):
#     return n*x
#
# sq = df['kor'].apply(gob,n=3)
# print(sq)
# print('-'*30)

def applyByColumn(col):
    print(col.shape)
    mysum = 0
    for item in col :
        mysum += item
    return mysum / col.shape[0]

print(df.apply(applyByColumn, axis=0))
print('-'*30)

def applyByColumn(row):
    print(row.shape)
    mysum = 0
    for item in row :
        mysum += item
    return mysum / row.shape[0]
print(df.apply(applyByColumn, axis=1))
print('-'*30)

savedfile = 'hohoho.csv'
df.to_csv(savedfile,encoding='utf-8')
print('파일이 저장되었습니다.')
print('-'*30)