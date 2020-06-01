import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')

filename = 'data/dataframeGraph.csv'
myframe = pd.read_csv(filename,encoding='euc-kr')

myframe.set_index(keys='name',inplace=True)
print(myframe)
myframe = myframe.T
myframe.plot(title='직원별 지역 실정',legend=True, figsize=(12,8), marker='o')
plt.legend(loc='best')
filename = 'data/dataframeGraph.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+'파일 저장 완료')

plt.show()