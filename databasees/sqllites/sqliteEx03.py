import sqlite3

# 생성자 : dbname(데이터베이스 이름)
# 소멸자 : 커서와 커넥션을 닫아 줍니다.
# 함수 : getJoindata() : 두테이블이 조인한 결과를 반환해주는 함수입니다.
#        getSubQuery(이름) : 해당 이름의 학생 성적 정보를 반환해주는 함수입니다.

class SqliteDB:
    def __init__(self,dbname):
        self.conn = sqlite3.connect(dbname)
        self.mycursor = self.conn.cursor()

    def __del__(self):
        self.mycursor.close()
        self.conn.close()

    def getJoindata(self):
        # 조인 sql
        sql = ' select st.id, st.name, st.birth, sg.subject, sg.jumsu'
        sql += ' from students st join sungjuk sg'
        sql += ' on st.id = sg.id'

        result = self.mycursor.execute(sql)
        return result
    #end def getJoindata

    def getSubQuery(self,name): #해당 이름의 학생 성적 정보를 반환해주는 함수
        sql = ' select * from sungjuk'
        sql += " where id = (select id from students where name = ?)"

        result = self.mycursor.execute(sql,(name,))

        return result

    def getJumsu(self,name): # 해당 학생의 점수 총점과 평균을 반환해주는 함수
        sql = " select sum(jumsu) as sum, avg(jumsu) as avg "
        sql += " from sungjuk where id =(SELECT id from students"
        sql += " where name = ?)"

        result = self.mycursor.execute(sql,(name,))
        return  result

#end class

dbname = 'sqlitedb.db'
mydb = SqliteDB(dbname)

dataset = mydb.getJoindata()
for row in dataset:
    print(f'아이디 : {row[0]}\n'
          f'이름 : {row[1]}\n'
          f'생일 : {row[2]}\n'
          f'과목 : {row[3]}\n'
          f'점수 : {row[4]}\n'
          f'-------------------')

who = '이승식'
dataset = mydb.getSubQuery(who)
for id,subject,jumsu in dataset:
    print(f'아이디 : {id}\n'
          f'과목 : {subject}\n'
          f'점수 : {jumsu}\n'
          f'----------------')

print('-'*30)

who = '고주몽'
who = '심형래'

dataset = mydb.getJumsu(who).fetchone()
if dataset[0] != None :
    print(f'총점 : {dataset[0]}\n'
          f'평균 : {dataset[1]:.2f}\n')
else:
    print('no')

print('finished')