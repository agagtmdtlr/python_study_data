import sqlite3
import csv
# 슈퍼 클래스
class SuperDao:
    def __init__(self,dbname):
        # print('슈퍼 생성자')
        self.conn = sqlite3.connect(dbname)
        self.mycursor = self.conn.cursor()

    def createTable(self):
        sql = '''create table departments
        (dno number , name text, locations text, tel text)'''
        self.mycursor.execute(sql)

        sql = '''create table employees
                (eid text o, name text, dno number, jikcode text, pay number, hiredate text, gender text)'''
        self.mycursor.execute(sql)

        sql = '''create table customers
                (cid number, name text, tel text, juminno text, eid text)'''
        self.mycursor.execute(sql)

    def getCsvData(self,csvfile):
        try:
            with open(file=csvfile,mode='r',encoding='euc-kr') as file :
                # 명시된 csv 파일을 읽어서 중첩 리스트로 반환합니다.
                mydata = csv.reader(file)
                totalist = [i for i in mydata]

                # totalist 0번째 요소는 header 부분이기 때문에 제외한다.
                return totalist[1:]
        except Exception:
            print('파일 없음')