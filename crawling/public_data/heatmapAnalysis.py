#상관 계수 시각화
import json
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from pandas import DataFrame

filename = 'data/immigrationTouristStat 중국(112)_(2015~2019).json'
myfile = open(filename,'rt',encoding='utf-8').read()
jsonfile = json.loads(myfile) # arg=str
print(type(jsonfile))
china_table = DataFrame(jsonfile,columns=('yyyymm','visit_cnt'))
# print(china_table.head())

# 문자를 날짜 타입으로
china_table.yyyymm = pd.to_datetime(china_table.yyyymm,format='%Y%m') # %Y:년도4자리 %m:월2자리

#dt : 날짜 타입에 들어있는 내장 객체 변수
china_table['year'] = china_table.yyyymm.dt.year
china_table['month'] = china_table.yyyymm.dt.month

china_table = china_table.set_index(['year','month'])

china_table = china_table['visit_cnt'].unstack(fill_value=0)
print(china_table.head())

# corr() : 상관 계수를 구해주는 gkatn
print(china_table.corr())

sns.heatmap(china_table.corr(method='spearman'))
plt.show()