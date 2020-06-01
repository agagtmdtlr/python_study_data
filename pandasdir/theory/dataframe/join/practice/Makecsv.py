import pandas as pd
from pandas import DataFrame

mydata = [('김철수',10),('박영희',20)]

with open(file='result02.csv',mode='w',encoding='utf-8') as file:
    for i in mydata:
        file.write(','.join(map(str,i))+'\n')

df = pd.read_csv('result02.csv',header=None)

print(df)
