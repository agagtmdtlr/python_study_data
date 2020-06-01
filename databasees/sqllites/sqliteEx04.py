import sqlite3

def getJoin(mycursor,db1,db2,key1,key2):
    sql = "select * from %s a join %s b "
    sql += " on a.%s = b.%s"

    result = mycursor.execute(sql %(db1,db2,key1,key2))

    return result
conn = sqlite3.connect('sqlitedb.db')
mycursor = conn.cursor()

try:
    mycursor.execute('drop table members')
    mycursor.execute('drop table boards')
except sqlite3.OperationalError as err:
    print('테이블이 존재하지 않음')

mycursor.execute('create table members'
                 '(id text, name text, gender text)')

mydata = [('hong','홍길동','남자'),
          ('park','박영희','여자')]

sql = "insert into members(id,name,gender)"
sql += " values(?,?,?)"
mycursor.executemany(sql,mydata)

mycursor.execute('create table boards'
                 ' (no integer, subject text, '
                 ' writer text, content text)')

mydata = [(1,'가가','hong','잼있어요'),
          (2,'나나','hong','조아요'),
          (3,'다다','hong','시러요'),
          (4,'라라','park','그래요'),
          (5,'마마','park','마자요'),
          (6,'바바','park','슬퍼요'),
          (7,'사사','park','행복해요')]

sql = "insert into boards(no,subject,writer,content)"
sql += " values(?,?,?,?)"
mycursor.executemany(sql,mydata)

conn.commit()
db1 = 'members'
db2 = 'boards'
key1 = 'id'
key2 = 'writer'

result = getJoin(mycursor,db1,db2,key1,key2)
for i in result:
    for x in i:
        print(x)
    print('-----')
