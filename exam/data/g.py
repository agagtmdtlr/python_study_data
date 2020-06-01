import pandas as pd
import matplotlib.pyplot as plt


myframe = pd.read_csv('plotStyleData.csv')

plt.plot(myframe.index,myframe,'og:',label='Hohoho')
plt.legend(loc='best')
plt.xlim(0,30)
filename = 'plotStyle.png'
plt.savefig( filename, dpi=400, bbox_inches='tight' )
print( filename + ' 파일이 저장되었습니다.')

plt.show()