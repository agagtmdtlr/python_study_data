import sqlite3

class MadangDB:
    def __init__(self):
        self.conn = sqlite3.connect('madang.db')
        self.mycursor = self.conn.cursor()

    def __del__(self):
        print('MadangDB 작업 종료')

    def creatBooks(self):
        try:
            self.mycursor.execute("create table books"
                                  "(no number, title text, publish text, price number)")
            self.conn.commit()
        except sqlite3.OperationalError as err:
            print('생성불가 : 테이블이 존재합니다')
    # end method createBooks

    def deleteTable(self):
        try:
            self.mycursor.execute("drop table books")
            self.conn.commit()
        except sqlite3.OperationalError as err:
            print('삭제불가 : 테이블이 존재하지 않습니다.')
    # end method deleteTable

    def insertData(self,datalist):
        sql = " insert into books(no,title,publish,price)" \
              " values (?,?,?,?)"
        try:
            for data in datalist:
                self.mycursor.execute(sql,data)
            self.conn.commit()
        except sqlite3.OperationalError as err:
            print(err)
    # end method insertData

    def getAllInfo(self):
        sql = " select * from books"
        results = self.mycursor.execute(sql)
        return results
    # end method getAllInfo
    def getKwdTitle(self,kwd):
        sql = " select * from books" \
              " where title like ?"
        results = self.mycursor.execute(sql,(kwd,))
        return results
    # end method getKwdTitle

    def showResult(self,result):
        for data in result:
            print(data)
    # end method showResult

# end class MadangDB

mdb = MadangDB()
mdb.deleteTable()
mdb.creatBooks()
datalist = [(1, '축구의 역사', '굿스포츠', 7000),
            (2, '축구아는 여자', '나무수', 13000),
            (3, '축구의 이해', '대한미디어', 22000),
            (4, '골프 바이블', '대한미디어', 35000),
            (5, '피겨 교본', '굿스포츠', 8000)]
mdb.insertData(datalist)
result = mdb.getAllInfo()
mdb.showResult(result)
result = mdb.getKwdTitle('%축구%')
mdb.showResult(result)