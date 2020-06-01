import pandas as pd

result = []

myencoding = 'utf-8'

mydata = [('김철수', 10), ('박영희', 20)]

myColumns = ['name','age']

result = mydata

myframe = pd.DataFrame(result, columns=myColumns)
print(myframe)
filename = 'result02.csv'
myencoding='utf-8'
myframe.to_csv(filename, encoding=myencoding, mode='w', index=False)