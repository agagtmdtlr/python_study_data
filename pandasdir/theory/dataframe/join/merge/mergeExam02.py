import pandas as pd

bbqfile = 'bbqmini.csv'

bbq = pd.read_csv(bbqfile, encoding='utf-8',index_col=0)
print(bbq)

districtfile = 'districtmini.csv'

district = pd.read_csv(districtfile, encoding='utf-8')
print(district)

result = pd.merge(bbq,district,on=['sido','gungu'],
               how='outer',suffixes=['','_'],indicator=True)
print(result)
print('-'*20)

m_result = result.query('_merge == "left_only"')
print('좌측에만 있는 행')
print(m_result)
print('-'*20)

# 전처리 보정 파일
with open('gungufile.txt',encoding='utf-8') as gungufile :
    gungu_lists = gungufile.readlines()

gungudict = {}
for onegu in gungu_lists:
    mydata = onegu.replace('\n','').split(':')
    gungudict[mydata[0]] = mydata[1]
print(gungudict)

bbq.gungu = bbq.gungu.apply(lambda data : gungudict.get(data,data))
print(bbq)