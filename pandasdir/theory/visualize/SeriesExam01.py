import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')

myindex = ['강감찬','홍길동','이순신','최영']

members = Series(data=[20,60,80,40],index=myindex)
print(members)

members.plot(kind='bar', rot=0, ylim=[0,100], use_index=True,
             color=['r','g','b','y'])

plt.xlabel('학생 이름')
plt.ylabel('점수', rotation=0)
plt.title('학생별 국어 시험')

ratio = 100 * members/members.sum() # 각 비율
print(ratio)
for idx in range(members.size):
    value = str(members[idx])+'건'
    # print(value)
    ratioval = '%.1f%%' %(ratio[idx])
    # print(ratioval)
    plt.text(x=idx,y=members[idx]+1, s=value, horizontalalignment='center')
    plt.text(x=idx, y=members[idx]/2, s=ratioval, horizontalalignment='center')

meanval = members.mean()
average = '평균 : %d건' %meanval
plt.axhline(y=meanval,color='r',linewidth=1,linestyle='--')
plt.text(x=0,y=meanval+1, s=average, horizontalalignment='center')
filename = 'data/graph01.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+'파일 저장 완료')

plt.show()