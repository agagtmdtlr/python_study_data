import numpy as np
import pandas as pd
from pandas import DataFrame

afile = 'android.csv'
bfile = 'iphone.csv'

atable = pd.read_csv(afile, index_col=0, encoding='utf-8')
btable = pd.read_csv(bfile, index_col=0, encoding='utf-8')

atable['phone'] = '안드로이드'
btable['phone'] = '아이폰'

print(atable)
print('-'*20)
print(btable)
print('-'*20)

result = pd.concat(objs=[atable,btable],ignore_index=True)
print(result)
filename = 'result.csv'

result.to_csv(filename,encoding='utf-8')
print(filename+'파일 저장')