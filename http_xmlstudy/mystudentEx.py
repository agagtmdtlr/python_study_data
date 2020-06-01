import sqlite3
from xml.etree.ElementTree import parse,Element
# with open('concat_data/mystudent.xml',mode='rt',encoding='utf-8-sig') as file:
#     mystr = file.read()
#     print(mystr)

tree = parse('concat_data/mystudent.xml')
students = tree.getroot()
print(len(students))


conn = sqlite3.connect('concat_data/student.db')
mycur = conn.cursor()

data = []
for item in students.findall('student'):
    print(type(item))
    if isinstance(item,Element):
        info = item.getchildren()
        row = [ x.text for x in info]
        data.append(row)

# 테이블 생성하기
sql = 'create table if not exists student' \
      ' ( name text primary key ,kor number,eng number,math number)'
mycur.execute(sql)
conn.commit()

# 테이블에 데이터 추가하기
sql = f'insert into student values(?,?,?,?)'
mycur.executemany(sql,data)
conn.commit()


# 저장된 데이터 불러오기
sql= 'select * from student'
for row in mycur.execute(sql):
    print(row)