from pandas import Series as sr
from pandas import DataFrame as df
import numpy as np

student = ['철수','영희','짱구','훈구','맹구']
series1 = sr(data=np.random.randint(30,50,size=len(student)),index=student)
print(series1)
print(f'value :\n'
      f'{series1.values}'
      f'type, value type :\n'
      f'{type(series1)}\n'
      f'{type(series1.values)}\n'
      f'count return Series :\n'
      f'{series1.value_counts()}\n'
      f'{type(series1.value_counts())}\n'
      f'index return Index obj : {series1.index}\n'
      f'items return zip :\n'
      f'{list(series1.items())}')

print(series1.add(series1))
print(series1.sub(series1))
print(series1.mul(series1))
print(series1.div(series1))