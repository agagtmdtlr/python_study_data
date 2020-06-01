import pandas as pd
import matplotlib.pyplot as plt

filename = 'data/plotStyleData.csv'
data = pd.read_csv(filename,header=None)

plt.rc('font',family='Malgun Gothic')
plt.plot(data, color='blue', marker='o', linestyle='dashed', label='호호호')
# 범례 보여주기.
plt.legend(loc='best')

filename = 'data/plotStyle.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename + '파일 저장 완료')
# plt.show()