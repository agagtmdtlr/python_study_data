import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import DataFrame, Series

plt.rc('font',family='Malgun Gothic')

filename = 'somedata2.csv'
myframe = pd.read_csv(filename,encoding='utf-8')
myframe.set_index('name',inplace=True)
print(myframe)

#1
# myframe.loc[:,'kor'].plot(kind='barh',rot=0)
# plt.xlabel('점수')
# plt.ylabel('학생',rotation=0)

#2
# myframe.loc[:,'kor'].plot(kind='bar',rot=0)
# plt.xlabel('학생')
# plt.ylabel('점수',rotation=0)

#3
# three = myframe.loc[myframe['gender']=='여자','math']
# plt.pie(three,labels=three.index,autopct='%.1f%%',startangle=90)
# plt.title('여자 수학 점수 파이 그래프')

#4
# four = myframe['gender'].value_counts()
# four.plot(kind='bar',rot=0,color=['r','g'])
# for i,j in enumerate(four):
#     print(i,j)
#     plt.text(i,j-1,str(j)+'명',fontsize=12,
#              horizontalalignment='center')

#5
# meancol = myframe.loc[:,['kor','eng','math']].mean(axis=1)
# myframe['pass'] = meancol.apply(lambda x : '합격'if x>=60 else'불합격')
# piepass = myframe['pass'].value_counts()
# plt.pie(piepass,labels=piepass.index,explode=[0.2,0],
#         autopct='%.2f%%',startangle=90,
#         counterclock=True,shadow=True)

#6
dfT = myframe.loc[:,['kor','eng','math']].T
ax = dfT.plot(kind='barh',rot=0,stacked=True)
count = 0
for p in ax.patches:
    left,bottom,width,height = p.get_bbox().bounds
    print(left,bottom,width,height)
    ax.annotate("%d" % (count), (left+width/2, bottom+height/2),ha='center')
    count += 1
plt.title('과목별 누적 가로 막대 그래프')

#7
# fm = myframe.loc[myframe['gender']=='남자']
# m = myframe.loc[myframe['gender']=='여자']
# print(fm.T)
# print(m['kor'].T)
# g = 0
# for i in ['kor','eng','math']:
#     plt.plot([g,g,g],fm[i],linestyle='None',marker='o',label='남자'+i)
#
# g = 1
# for i in m.loc[:,['kor','eng','math']]:
#     plt.plot([g,g,g],m[i],linestyle='None',marker='o',label='여자'+i)

plt.legend()
filename = 'data/makeGraph06.png'
plt.savefig(filename, dpi=400, bbox_inches='tight')
print(filename+'파일 저장 완료')
#
#
plt.show()