from xml.etree.ElementTree import parse
from pandas import DataFrame

filename = 'data/inchon_data.xml'

tree = parse(filename) # element tree
myroot = tree.getroot()
print(type(myroot)) # super element
print('-'*20)

allstores = myroot.findall('Row')
print(type(allstores)) # type list
print(len(allstores))

allShopInfo = [] # 전체 데이터 저장소

for store in allstores:
    # store type : element
    childs = store.getchildren() # childs list[element]
    shopInfo = [] # 1매장의 정보가 들어갈 리스트
    for child in childs :
        # child : element
        mydata = child.text.replace(',','') # get element text
        mydata = mydata.replace('"','')
        # print(mydata)
        shopInfo.append(mydata)
    allShopInfo.append(shopInfo)
    # print('-'*20)

mycolumns = ['업소명','소재지 도로명','전화 번호','주된 음식']
myframe = DataFrame(allShopInfo,columns=mycolumns)
# print(myframe.head())

savedfile = 'concat_data/data_inchon.csv'
myframe.to_csv(savedfile,encoding='EUC-KR') # excel확인은 euc-kr
print(savedfile + '파일이 저장되었습니다.')

import sqlite3

dbfilename = 'concat_data/inchon.db'
conn = sqlite3.connect(dbfilename)

mycursor = conn.cursor()

try:
    sql = 'drop table inchon'
    mycursor.execute(sql)
except sqlite3.OperationalError:
    print('테이블 존재하지 않습니다.')

sql = '''create table inchon(name text primary key,
 roadname text, phone text, maindish text)'''
mycursor.execute(sql)

for onedata in range(len(myframe)):
    imsi = myframe.iloc[onedata]
    name = imsi['업소명']
    roadname = imsi['소재지 도로명']
    phone = imsi['전화 번호']
    maindish = imsi['주된 음식']

    sql = "insert into inchon values(?,?,?,?)"
    mycursor.execute(sql,(name,roadname,phone,maindish))

conn.commit()

finddata = '신세계'
sql = "select * from inchon where name like '%"+finddata+"%'"

print(f'업소 이름 [{finddata}]라는 글자가 들어간 업체')

for row in mycursor.execute(sql):
    print(row)
print('-'*20)

finddata = '백숙'
sql = "select * from inchon where maindish like '%"+finddata+"%'"

print(f'주된 음식이 [{finddata}]인 업체')

for row in mycursor.execute(sql):
    print(row)
print('-'*20)

finddata = 'name'
sql = "select * from inchon order by {}".format(finddata)

print(f'[{finddata}] 기준으로 업체 정렬')

for row in mycursor.execute(sql):
    print(row)
print('-'*20)

mycursor.close()
conn.close()



print('finished')