import sqlite3

#파일 불러오기
filename = 'saram.txt'
myfile = open(file=filename,mode='r',encoding='utf')

getlines = myfile.readlines()
mydata = [tuple(i.strip().split(',')) for i in getlines]
print(mydata)

myfile.close()

#테이블 작업
dbname = 'saram.db'
conn = sqlite3.connect(dbname)
mycursor = conn.cursor()

mycursor.execute("drop table mem")
mycursor.execute("create table mem("
                 "id number, msg text, name text, comment text)")

#데이터 삽입:
sql = "insert into mem(id,msg,name,comment)" \
      " values(?,?,?,?)"
for item in mydata:
    mycursor.execute(sql,item)

conn.commit()