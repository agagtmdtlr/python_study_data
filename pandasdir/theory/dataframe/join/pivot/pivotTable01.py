import pandas as pd

filename = 'pivotFile.csv'
data = pd.read_csv(filename,encoding='utf-8')
print(data)
print('-'*20)

pivotData = data.pivot(index='name',columns='item',values='value')
print(pivotData)
print('-'*20)
