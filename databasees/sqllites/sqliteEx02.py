import sqlite3


def getAllInfo(mycursor):
    for onetuple in mycursor:
        print(f'아이디 : {onetuple[0]}\n'
              f'이름 : {onetuple[1]}\n'
              f'점수 : {onetuple[2]}'.replace('\n',' '))
    print('-'*50)
conn = sqlite3.connect('sqlitedb.db')
mycursor = conn.cursor()

try:
    mycursor.execute('drop table sungjuk')
except sqlite3.OperationalError as err:
    print('테이블이 존재하지 않습니다.')

mycursor.execute('''create table sungjuk
    (id text, subject text, jumsu integer)''')

mycursor.execute("insert into sungjuk values('lee','java',10)")
mycursor.execute("insert into sungjuk values('lee','html',20)")
mycursor.execute("insert into sungjuk values('lee','python',30)")

sql = "insert into sungjuk values(?,?,?)"
datalist = [('jo','java',40),('jo','html',50),('jo','python',60),\
            ('ko','java',70),('ko','html',80),('ko','python',90)]
mycursor.executemany(sql,datalist)

conn.commit()

sql = 'select * from sungjuk'
mycursor.execute(sql)
getAllInfo(mycursor)

# print(mycursor)
# print(mycursor.arraysize)

sql = 'select * from sungjuk order by subject desc, jumsu asc'
mycursor.execute(sql)
getAllInfo(mycursor)
mycursor.close()
conn.close()

