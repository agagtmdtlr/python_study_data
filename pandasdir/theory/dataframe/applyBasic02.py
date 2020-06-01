import pandas as pd
from pandas import DataFrame,Series

filename='D:\pss\python\project1\pyy\data\sampledata.csv'
df = pd.read_csv(filename)
df.to_csv('sampledata.csv',encoding='utf-8')
df.index = [ chr(65+i) for i in range(df.index.shape[0])]



def genderEncoding(gender):
    elist = ['남자','여자']
    return elist[gender-1]


def ageEncoding(age):
    elist = ['','','20','30','40','50']
    return elist[age//10]+'대'

df.loc[:,'gender'] = df['gender'].apply(genderEncoding)
df.loc[:,'age'] = df['age'].apply(ageEncoding)

jobs = ['의사','변호사']
types = ['일반인 광고','연예인 광고']
categorys = ['운동','여행','게임','컴퓨터']
for i in (1,2):
    # cond = df['job'] == i # 올바른 예시
    # df.loc[cond, 'job'] = jobs[i-1] # 올바른 예시
    df['job'].loc[df['job'] == i] = jobs[i-1] # 잘못된 예시
    cond = df['type'] == i
    df.loc[cond, 'type'] = types[i - 1]
for i in (1,2,3,4):
    cond = df['category'] == i
    df.loc[cond,'category'] = categorys[i - 1]

print(df.loc[df['gender']=='남자'])
print(df.loc[df['gender']=='여자',['gender','age','job']])
cond1 = df['amount'] >= 45
cond2 = df['amount'] <= 65

condf = DataFrame((cond1,cond2))
print(df.loc[condf.all()])
def amountcoding(x):
    if x >= 45 and x <= 65:
        return True
    return False
def Conding(x,n):
    if x in n:
        return True
    else :
        return False
cond1 = df['amount'].apply(amountcoding)
cond2 = df['age'].apply(Conding,n=('20대','30대'))
condf = DataFrame((cond1,cond2))
print(condf.all())
print(df.loc[condf.all()])

cond = df['category'].apply(Conding,n=('운동','게임'))
print(df.loc[cond])

df.loc[df['job']=='의사','job'] = '판사'
print(df['job'])

def Grading(x):
    if x >= 90:
        return '수'
    elif x >= 80:
        return '우'
    elif x >= 70:
        return '미'
    elif x >= 60:
        return '양'
    else:
        return '가'

df.loc[:,'grade'] = df['amount'].apply(Grading)
print(df)

df.to_csv('resultdata.csv')