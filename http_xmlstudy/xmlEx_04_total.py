from xml.etree.ElementTree import parse,Element
import sqlite3
import re

tree = parse('concat_data/xmlEx_04_total.xml')
print(tree)
lists = tree.getroot()
print(lists)

data = []
if isinstance(lists,Element):
    items = lists.findall('item')
    print(type(items))
    for item in items:
        row = [x.text for x in item.getchildren()]

        ##########################################
        # fail_case
        # lens = 0 # 슬라이싱에 사용
        # 상위주소는 제외하고 뒤에 상세주소만을 확인하기 위함
        # infos = item.getchildren() # return list
        # element.text로 변수 저장
        # store = infos[0].text
        # sido = infos[1].text
        # gungu = infos[2].text
        # road = infos[3].text
        # lens += sum([len(x.text) for x in infos[1:2]])
        # imsi = infos[3].text.split(' ')[2:]
        # lens += sum([len(x) for x in imsi])
        # detailadd = infos[4].text[lens:]
        # local_code = infos[5].text
        # tel_no = infos[6].text
        # sub = infos[7].text
        ########################################################

        # reg_ex = f'^{sido}{gungu}'
        # patter = re.compile(reg_ex)
        # result = patter.search(infos[4].text)
        # print(result)
        # print(lens)
        # print(row)
        # case1
        data.append(row)
        # case2
        # concat_data.append([store,sido,gungu,road,detailadd,local_code,tel_no,sub])

conn = sqlite3.connect('concat_data/xmlEx_04_total.db')
mycur = conn.cursor()

sql = 'drop table if exists addresses'
mycur.execute(sql)
conn.commit()

sql = 'create table if not exists addresses' \
      ' ( store text, sido text, gungu text, road text, ' \
      ' fulladd text, local_code number, tel_no text , sub number )'
mycur.execute(sql)
conn.commit()

sql = ' insert into addresses values(?,?,?,?,?,?,?,?)'
mycur.executemany(sql,data)
conn.commit()

sql = 'select * from addresses'
# for row in mycur.execute(sql):
#     print(row)