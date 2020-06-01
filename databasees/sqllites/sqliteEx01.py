import sqlite3

conn = sqlite3.connect('sqlitedb.db')

mycursor = conn.cursor()

#work contents

try:
    mycursor.execute("drop table students")
except sqlite3.OperationalError as err:
    print('테이블이 존재하지 않습니다.')

#create table
mycursor.execute('''create table students
    (id text primary key, name text, birth text)''')
#insert concat_data
mycursor.execute("insert into students(id, name, birth) values('lee','이승식','1984/12/11')")
mycursor.execute("insert into students(id, name, birth) values('jo','조권','1984/12/11')")

datamylist = [('ko','고주몽','1234/08/14'),\
              ('sim','심형래','1995/09/20'),\
              ('kim','김유신','0500/01/21')]

sql = "insert into students(id, name, birth) values(?,?,?)"

mycursor.executemany(sql, datamylist)

conn.commit()

findid = 'ko'
sql = "select * from students where id = '%s'"
mycursor.execute(sql %(findid))

result = mycursor.fetchone()
print(f'아이디 : {result[0]}\n'
      f'이름 : {result[1]}\n'
      f'생일 : {result[2]}\n')
# for row in mycursor.fetchone():

sql = 'select * from students order by name desc'
for row in mycursor.execute(sql):
    print(row)

for id,name,birth in mycursor.execute(sql):
    print(id+'/'+name+'/'+birth)

sql = "select * from students where name like'%이%'"
mycursor.execute(sql)
print(mycursor.fetchall())
print('-'*20)

sql = "update students set name='%s' where id = '%s'"
pid = 'kim'
newname= '김춘추'
mycursor.execute(sql %(newname,pid))

conn.commit()

sql = "delete from students where id = '%s'"
pid = 'sim'
mycursor.execute(sql %(pid))

conn.commit()

mycursor.close()
conn.close()

print('finished')