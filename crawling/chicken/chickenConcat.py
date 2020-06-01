import pandas as pd
import numpy as np
from pandas import  DataFrame

myencoding ='utf-8'
chickenList = ['cheogajip','goobne','kyochon','pelicana','nene']

newframe = DataFrame()

for onestore in chickenList:
    filename = 'studydata/'+onestore+'.csv'
    myframe = pd.read_csv(filename,index_col=0,encoding=myencoding)
    newframe = pd.concat([newframe,myframe],axis=0,ignore_index=True)

print(newframe.head())
print('-'*50)
print(newframe.info())

totalfile = 'studydata/allstore.csv'
newframe.to_csv(totalfile,encoding=myencoding)
print(totalfile+' 파일 저장 완료')
print('finished')