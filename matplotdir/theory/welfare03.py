import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')
matplotlib.rcParams['axes.unicode_minus'] = False # 마이너스 기호 깨짐 방지

filename = 'data/welfare_python.csv'
welframe = pd.read_csv(filename,encoding='utf-8')
welframe.info()
print('-'*30)

job_file = 'data/welfare_job.csv'
jobframe = pd.read_csv(job_file,encoding='cp949') #완성형 조합코드
jobframe.info()
print('-'*30)

print(welframe['code_job'].unique())

newframe = pd.merge(welframe,jobframe,on='code_job')

ageg_income = newframe.dropna(subset=['income','job'])
mygrouping = ageg_income.groupby(by='job')['income']
mydata = mygrouping.mean()
newdata = mydata.sort_values(ascending=False).head(10)
print(mydata)
print(newdata)
newdata.plot(kind='barh',rot=0)

plt.xlabel('평균 소득')
plt.ylabel('직업')
plt.title('직업별 평균 소득 top 10')

filename = 'welfare_03_01.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')

newdata = mydata.sort_values().head(10)
newdata.plot(kind='pie',startangle=90,autopct='%.2f%%',
             counterclock=False,explode=[0.1]*10,shadow=True)
plt.xlabel('')
plt.ylabel('')
plt.title('직업 하위 순위 10')

filename = 'welfare_03_02.png'
plt.savefig(filename,dpi=400, bbox_inches='tight')
plt.figure()
print(filename + '파일 저장 완료')