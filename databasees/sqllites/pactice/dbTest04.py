# Customer 데이터 넣은 후 조회
from pyy.databasees.sqllites.pactice.subClass import Customer

cus = Customer('mall.db','customers.csv')

cus.delete()
cus.insert()
mydata = cus.getAllData()
for i in mydata:
    print(i)