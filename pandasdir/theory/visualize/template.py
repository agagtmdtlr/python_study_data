import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

filename = 'data/aaa.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+'파일 저장 완료')

#plt.show()