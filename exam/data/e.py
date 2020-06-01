import pandas as pd

afile = pd.read_csv('android.csv',index_col=0)
bfile= pd.read_csv('iphone.csv',index_col=0)

afile['phone'] = '안드로이드'
bfile['phone'] = '아이폰'
result = pd.concat([afile,bfile])
print(result)

filename = 'result.csv'
result.to_csv( filename , encoding='utf-8')
print(filename + ' 저장 완료')