import pandas as pd
import numpy as np

filename = 'excel01.csv'
myframe = pd.read_csv(filename,index_col='이름')
print(myframe.shape)
print(myframe)
print('-'*40)

print(myframe.fillna(value=0,inplace=True)) # inplace 변화값 저장
print(myframe)

myframe.iloc[0:2,0:2] = np.nan
myframe.loc['박영희':,'수학'] = np.nan
print(myframe)

mydict = {'국어':15,'영어':25,'수학':35}
print(myframe.fillna(value=mydict, inplace=True))

myframe.iloc[2,0] = np.nan
myframe.iloc[1,1] = np.nan
myframe.iloc[3,2] = np.nan
print(myframe)

mydict = {'국어':myframe['국어'].mean(),
          '영어':myframe['영어'].mean(),
          '수학':myframe['수학'].mean()}
myframe.fillna(value=mydict, inplace=True)
print(myframe)
