from pyy.databasees.sqllites.pactice.superClass import SuperDao
# 서브 클래스
class Department(SuperDao):
    def __init__(self, dbname,csvfile=None):
        super().__init__(dbname)
        if csvfile:
            self.csvdata = self.getCsvData(csvfile)

        # print(self.csvdata)

    def insert(self):
        sql = " insert into departments(dno,name,locations,tel) " \
              " values(?,?,?,?)"
        self.mycursor.executemany(sql,self.csvdata)
        self.conn.commit()

    def update(self,dno,name):
        sql = " update departments set name = ? "
        sql += " where dno = ? "
        self.mycursor.execute(sql,(name,dno))
        self.conn.commit()

    def getAllData(self):
        sql = " select * from departments order by name asc"
        return self.mycursor.execute(sql)
# end class Department

class Employee(SuperDao):
    def __init__(self,dbname,csvfile=None):
        super().__init__(dbname)
        if csvfile:
            self.csvdata = super().getCsvData(csvfile)

    def insert(self):
        sql = " insert into employees(eid,name,dno,jikcode,pay,hiredate,gender)" \
              " values (?,?,?,?,?,?,?)"
        self.mycursor.executemany(sql,self.csvdata)
        self.conn.commit()

    def delete(self):
        sql = " delete from employees"
        self.mycursor.execute(sql)
        self.conn.commit()

    def update(self,eid,jikcode):
        sql = " update employees set jikcode = ? " \
              " where eid = ? "
        self.mycursor.execute(sql,(jikcode,eid))
        self.conn.commit()

    def getAllData(self):
        sql = " select * from employees order by name asc"
        return self.mycursor.execute(sql)

# end class Employee

class Customer(SuperDao):
    def __init__(self,dbname,csvfile=None):
        super().__init__(dbname)
        if csvfile:
            self.csvdata = super().getCsvData(csvfile)

    def insert(self):
        sql = " insert into customers(cid,name,tel,juminno,eid)" \
              " values (?,?,?,?,?)"
        self.mycursor.executemany(sql,self.csvdata)
        self.conn.commit()

    def delete(self):
        sql = " delete from customers"
        self.mycursor.execute(sql)
        self.conn.commit()

    def update(self,cid,tel):
        sql = " update customers set tel = ? " \
              " where cid = ? "
        self.mycursor.execute(sql,(tel,cid))
        self.conn.commit()

    def getAllData(self):
        sql = " select * from customers order by name asc"
        return self.mycursor.execute(sql)
# end class Customer


class Composite(SuperDao): #조인 구문 서브 쿼리
    def __init__(self,dbname):
        super().__init__(dbname)

    def getData(self): # 부서, 직원 테이블 조인하여 부서명 순으로 정렬하여 보여주기
        sql = " select d.name dname, e.name ename, e.jikcode "
        sql += " from departments d join employees e on d.dno = e.dno "
        sql += " order by d.name "
        return self.mycursor.execute(sql)

    def getData2(self,who): # 직원별 고객정보
        sql = " select cid, name, tel from customers "
        sql += " where eid in (select eid from employees where name =?) "
        return self.mycursor.execute(sql,(who,))

    def getData3(self,who): # 부서별 직원들의 고객 정보
        sql = " select cid,name,tel " \
              " from customers " \
              " where eid in ( " \
              "     select eid from employees where dno = " \
              "     (select dno from departments where name= ?) " \
              " ) "
        return self.mycursor.execute(sql, (who,))