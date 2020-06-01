# Employee 데이터 넣은 후 조회
from pyy.databasees.sqllites.pactice.subClass import Employee
emp = Employee('mall.db','employees.csv')

emp.delete()
emp.insert()
mydata = emp.getAllData()
for i in mydata:
    print(i)
